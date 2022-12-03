from django import forms
from .models import posts

class postsform(forms.ModelForm):
    class Meta:
        model = posts
        fields = ('title','content','Post_date')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'Post'}),
            'content': forms.Textarea(attrs={'class':'Post'}),
        }

class sendMail(forms.Form):
    title = forms.CharField(max_length="20",widget=forms.TextInput(attrs={'class':'tunghoa','id':'title'}))
    mail = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'tunghoa','id':'content'}))
