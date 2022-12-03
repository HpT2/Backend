from django.urls import path
from . import views

app_name = 'new'
urlpatterns = [
    path('', views.redirect,name = 'new'),
    path('post/',views.postform,name = 'post'),
    path('post/posted/',views.posted, name = 'posted'),
    path('mail/',views.Mail,name = 'mail'),
    path('mail/mailed',views.Mailed,name = 'mailed')
]