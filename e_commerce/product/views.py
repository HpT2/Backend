from django.shortcuts import render
from django.http import  HttpResponse
from .models import Product
from .forms import NewProductForm
from django.db import connection
from .models import Product
# Create your views here.


def change_info_page(request):
    a = Product.objects.all()
    return render(request,'product/change_info_page.html',{'product_info': a})


def change_product_info(request,product_id ):
    product = Product.objects.get(product_id=product_id)
    return render(request,'product/change_produt_info.html', {'product': product})


def postnewproduct(request):
    a = NewProductForm()
    return render(request,'product/newproduct.html',{'form':a})


def newproduct(request):
    if(request.method == 'POST'):
        data = NewProductForm(request.POST)
        if(data.is_valid()):
            p_data = data.cleaned_data
            try:
                cursor = connection.cursor()
                query = 'EXEC product.insert_product @product_id={0}, @product_name={1},' \
                        '@product_desc={2}, @price={3},@amount={4}, @category_id={5},' \
                        '@admin_id={6},@product_img={7}'.format(p_data['product_id'],
                                                                        p_data['product_name'], p_data['product_desc'],
                                                                        p_data['price'],p_data['amount'], p_data['category_id'],
                                                                        p_data['admin_id'], p_data['product_img'])
                cursor.execute(query)
                return HttpResponse('ok')
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse('Notvalid')

