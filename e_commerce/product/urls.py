from . import views
from django.urls import path

app_name = 'product'
urlpatterns = [
    path('', views.test, name='test'),
    path('newproduct/', views.postnewproduct, name='post'),
    path('newproduct/posted', views.newproduct, name='posted')
]