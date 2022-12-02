from django.contrib import admin
from .models import Customer,Cart,Contain,Feedback,Orders
# Register your models here.
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Contain)
admin.site.register(Feedback)
admin.site.register(Orders)