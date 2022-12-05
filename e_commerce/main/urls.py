from . import views
from django.urls import path,include
app_name = 'main'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('Addmin/', views.login_admin, name='login_admin'),
    path('Admin/home', views.login_admin_res, name = 'login_admin_res'),
    path('customer/', views.login_customer, name='login_customer'),
    path('signup/', views.signup_page, name='signup_page'),
]