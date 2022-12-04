from . import views
from django.urls import path
app_name = 'service'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('/register', views.register, name="register")
]