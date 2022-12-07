from django.shortcuts import render
from django.http import  HttpResponse
from .models import Product
from .forms import NewProductForm
from django.db import connection
from .models import Product
# Create your views here.


def change_info_page(request):
    if(request.method=='POST' and 'Edit' in request.POST):
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