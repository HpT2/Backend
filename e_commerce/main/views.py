from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from service.models import Customer
from django.db import connection
from service.views import homepage
from management.views import admin_home
# Create your views here.


def login_customer(request,error=None):
    form = LoginForm()
    return render(request,'main/login_customer.html', {'form': form,'error':error})


def home(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        cursor = connection.cursor()
        query = 'exec  [service].[authentication] @username="{0}", @password="{1}"' \
            .format(username, password)
        try:
            cursor.execute(query)
        except Exception as e:
            cursor.close()
            error = 'Sai tên đăng nhập hoặc mật khẩu'
            return login_customer(request,error)
        cursor.close()
        request.session['username'] = username
        return homepage(request)
    else:
        return homepage(request)


def signup_page(request):
    return render(request, 'main/signup.html')


def login_admin(request,error=None):
    form = LoginForm()
    return render(request, 'main/login_admin.html', {'form': form,'error':error})



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
            error = 'Sai tên tài khoản hoặc mật khẩu'
            return login_admin(request,error)
        cursor.close()
        request.session['username'] = username
        return admin_home(request)
    else:
        return HttpResponse("You have not login")
