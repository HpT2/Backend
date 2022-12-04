from django.shortcuts import render

# Create your views here.


def admin_home(request,username):
    request.session['username'] = username
    return render(request,'management/admin_home.html')


