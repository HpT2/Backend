from .models import Login
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

