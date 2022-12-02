from django.shortcuts import render
from django.http import  HttpResponse
from .models import Product
from .forms import NewProductForm
from django.db import connection
# Create your views here.


def test(request):
    product = Product.objects.get(product_id=1)
    return render(request, 'product/test.html', {'item': product})


def postnewproduct(request):
    a = NewProductForm()
    return render(request,'product/newproduct.html',{'form':a})


def newproduct(request):
    if(request.method == 'POST'):
        data = NewProductForm(request.POST)
        if(data.is_valid()):
            p_data = data.cleaned_data
            cursor = connection.cursor()
            query = 'EXEC product.insert_product @product_id={0}, @product_name={1},' \
                    '@product_desc={2}, @price={3},@amount={4}, @category_id={5},' \
                    '@admin_id={6},@product_img={7}'.format(p_data['product_id'],
                                                                    p_data['product_name'], p_data['product_desc'],
                                                                    p_data['price'],p_data['amount'], p_data['category_id'],
                                                                    p_data['admin_id'], p_data['product_img'])
            cursor.execute(query)
            return HttpResponse('ok')
        else:
            return HttpResponse('Notvalid')

