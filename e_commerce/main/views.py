from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.db import connection
from service.views import homepage
from management.views import admin_home
# Create your views here.


def login_customer(request):
    form = LoginForm()
    return render(request,'main/login_customer.html', {'form': form})


def home(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        cursor = connection.cursor()
        query = 'exec  [service].[authentication] @username="{0}", @password="{1}"' \
            .format(username, password)
        print(query)
        cursor.execute(query)
        res = cursor.fetchall()
        if (len(res) == 0):
            cursor.close()
            return HttpResponse("No user")
        cursor.close()
        return homepage(request, username)
    else:
        return homepage(request)


def signup_page(request):
    return render(request, 'main/signup.html')


def login_admin(request):
    form = LoginForm()
    return render(request, 'main/login_admin.html', {'form': form})



def login_admin_res(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        cursor = connection.cursor()
        query = 'exec  [management].[authentication] @username="{0}", @password="{1}"'\
            .format(username, password)
        print(query)
        cursor.execute(query)
        res = cursor.fetchall()
        if(len(res)==0):
            cursor.close()
            return HttpResponse("No user")
        cursor.close()
        return admin_home(request,username)
    else:
        return HttpResponse("You have not login")
