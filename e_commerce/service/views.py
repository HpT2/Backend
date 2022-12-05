from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Customer
# Create your views here.


def homepage(request):
    try:
        username = request.session['username']
    except:
        username = None
    return render(request, 'service/homepage.html', {'username': username})



def shop_page(request):
    username = request.session['username']
    return render(request, 'service/shop-grid.html', {'user': username} )


<<<<<<< Updated upstream
def cart_page(request):
    username = request.session['username']
    return render(request, 'service/shoping-cart.html', {'user': username} )
=======
def cart_page(request,  username=None): 
    request.session['username'] = username
    return render(request, 'service/shoping-cart.html', {'user': username})

>>>>>>> Stashed changes

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
    return render(request,'service/profile.html', {'user':user})


def logout(request):
    if(request['username'] != None):
        del request.session['username']
        return HttpResponse("<strong>You are logged out.</strong>")