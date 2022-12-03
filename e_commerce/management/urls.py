from . import views
from django.urls import path, include
app_name = 'main'
urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('/newproduct',views.addproduct, name='add_product'),
]