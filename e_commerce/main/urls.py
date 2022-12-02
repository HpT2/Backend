from . import views
from django.urls import path
app_name = 'main'
urlpatterns = [
    path('', views.login, name='login'),
    path('/home', views.homepage, name='home'),
    path('/login_res', views.login_res, name='login_res'),
]