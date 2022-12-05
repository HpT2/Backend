from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from .models import Customer
from product.models import Product
# Create your views here.


def homepage(request):
    try:
        username = request.session['username']
    except:
        username = None
    return render(request, 'service/homepage.html', {'username': username})



def shop_page(request):
    product_list = Product.objects.all()
    try:
        username = request.session['username']
    except:
        username = None
    return render(request, 'service/shop-grid.html', {'username': username,'product_list':product_list} )


def cart_page(request):
    try:
        username = request.session['username']
    except:
        username = None
    return render(request, 'service/shoping-cart.html', {'username': username} )



def register(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email']
        Phone = '09714799331'
        Address = 'sdsadasdad'
        query = 'exec service.register @Fname="{0}", @Lname="{1}", @username="{2}", @password="{3}", ' \
                '@Email="{4}", @Phone="{5}", @Address="{6}"'.format(Fname,Lname,username,password,Email,Phone,Address)
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            cursor.close()
            return HttpResponse("Register success")
        except Exception as e:
            print(e)
            cursor.close()
            return HttpResponse(e)


def profile(request):
    username = request.session['username']
    user = Customer.objects.get(username=username)
    if(request.method == 'POST'):
        address = request.POST['address']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['email']
        Birthdate = request.POST['Birthdate']
        query = 'exec service.update_info @username={0}, @address="{1}", @Fname={2}, @Lname={3}, ' \
               '@Email="{4}", @Birthdate="{5}"'.format(username,address,Fname,Lname,Email,Birthdate)
        cursor = connection.cursor()
        try:
            print(query)
            cursor.execute(query)
            cursor.close()
            username = request.session['username']
        except:
            error = 'cannot save'
            return render(request,'service/profile.html', {'user':user,'error':error})
    return render(request,'service/profile.html', {'user':user})


def logout(request):
    del request.session['username']
    return homepage(request)
