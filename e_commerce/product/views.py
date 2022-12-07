from django.shortcuts import render
from django.http import  HttpResponse
from .models import Product
from .forms import NewProductForm
from django.db import connection
from .models import Product
# Create your views here.


def change_info_page(request):
    if(request.method=='POST'):
        if('Edit' in request.POST):
            print(request.FILES)
            query = 'delete product.product\n' \
                    'where product_id={0}'.format(request.POST['product_id'])
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                return HttpResponse(e)
            data = NewProductForm(data=request.POST, files=request.FILES)
            if (data.is_valid()):
                data.save()
    a = Product.objects.all()
    return render(request,'product/change_info_page.html',{'product_info': a})



def postnewproduct(request, product=None):
    a = NewProductForm()
    return render(request,'product/newproduct.html',{'form':a,'product':product})


def newproduct(request):
    if(request.method == 'POST'):
        data = NewProductForm(data=request.POST, files=request.FILES)
        if(data.is_valid()):
           data.save()
           return postnewproduct(request)
        else:
            return HttpResponse('Notvalid')


def edit(request):
    product = Product.objects.get(product_id=request.POST['product_id'])
    return postnewproduct(request, product)

def remove(request):
    query = 'delete product.product where product_id={0}'.format(request.POST['product_id'])
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    return change_info_page(request)

def category(request):
    error = None
    if(request.method=='POST'):
        if 'add_button' in request.POST:
            id = request.POST['category_id']
            name = request.POST['category_name']
            if(id=="" or name==""):
                error = "You must fill all fields to add new category"
            query="insert into product.category(category_id,category_name)\n" \
                  "values ({0},'{1}')".format(id, name)
            cursor=connection.cursor()
            try:
                cursor.execute(query)
            except:
                error = 'ID existed'
            cursor.close()
        if 'remove_button' in request.POST:
            id = request.POST['category_id']
            name = request.POST['category_name']
            if(id=="" and name==""):
                error = "Fill id or name to remove a category"
            if(name==""):
                query = 'delete product.category\n' \
                        'where category_id={0}'.format(id)
            else:
                query = "delete product.category\n "\
                        "where category_name='{0}'".format(name)
            cursor = connection.cursor()
            try:
                cursor.execute(query)
            except Exception as e:
                error = e
            cursor.close()
    return render(request,'product/category.html',{'error':error})

