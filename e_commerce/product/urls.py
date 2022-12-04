from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [
    path('newproduct/', views.postnewproduct, name='Add'),
    path('change_info/', views.change_info_page, name='Change_info'),
    path('change_info/<int:product_id>',views.change_product_info,name='change_product_info'),
    path('newproduct/posted', views.newproduct, name='posted'),
]