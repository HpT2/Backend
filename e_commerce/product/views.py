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
        data = NewProductForm(data=request.POST, files=request.FILES)
        if(data.is_valid()):
           data.save()
           return postnewproduct(request)
        else:
            return HttpResponse('Notvalid')

