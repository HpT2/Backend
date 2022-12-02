from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.db import connection
# Create your views here.


def homepage(request):
    return render(request, 'main/homepage.html')


def login(request):
    form = LoginForm()
    return render(request, 'main/log_in.html', {'form': form})


def login_res(request):
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
        return homepage(request)
