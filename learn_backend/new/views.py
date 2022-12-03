from django.shortcuts import render
from django.http import  HttpResponse
from .forms import postsform,sendMail
# Create your views here.


def redirect(request):
    return render(request,"new/rec.html")


def postform(request):
    a = postsform()
    return render(request,'new/new.html',{'fields':a})


def posted(request):
    if(request.method == 'POST'):
        p_data = postsform(request.POST)
        if(p_data.is_valid()):
            p_data.save()
            return HttpResponse('posted')
        else:
            return HttpResponse('Notvalid')
    else:
        a = postsform()
        return render(request,'new/new.html',{'fields':a})

def Mail(request):
    a = sendMail()
    return render(request,'new/mail.html',{'fields':a})

def Mailed(request):
    if (request.method == 'POST'):
        mail_data = sendMail(request.POST)
        if (mail_data.is_valid()):
            return render(request,'new/mailed.html',{'fields':mail_data})
        else:
            return HttpResponse('Notvalid')
    else:
        a = sendMail()
        return render(request, 'new/mail.html', {'fields': a})