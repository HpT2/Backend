from . import views
from django.urls import path
app_name = 'service'
urlpatterns = [
    path('', views.homepage, name='homepage'),
<<<<<<< Updated upstream
    path('/register', views.register, name="register"),
    path('profile',views.profile, name='profile'),
=======
    path('register', views.register, name="register"),
>>>>>>> Stashed changes
    path('shop', views.shop_page, name='shop_page'),
    path('cart', views.cart_page, name='cart_page')
]