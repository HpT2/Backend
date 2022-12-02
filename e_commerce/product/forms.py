from django import forms
from .models import Product


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        def getimg(self, img):
            self.model['product_img'] = img
