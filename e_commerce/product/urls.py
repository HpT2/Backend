from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [
    path('newproduct/', views.postnewproduct, name='Add'),
    path('change_info/', views.change_info_page, name='Change_info'),
    path('change_info/edit', views.edit, name='Edit_form'),
    path('newproduct/posted', views.newproduct, name='posted'),
    path('remove',views.remove,name='remove'),
    path('category',views.category,name='category'),
]