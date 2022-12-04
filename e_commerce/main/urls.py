from . import views
from django.urls import path,include
app_name = 'main'
urlpatterns = [
    path('admin_login/', views.login_admin, name='login_admin'),
    path('', include('service.urls'), name='homepage'),
    path('customer/', views.login_customer, name='login_customer'),
    path('signup/', views.signup_page, name='signup_page'),
    path('login_customer_res/', views.login_customer_res, name='login_customer_res'),
    path('login_customer_res/service', include("service.urls"), name='service'),
    path('login_admin_res/', views.login_admin_res, name='login_admin_res'),
]