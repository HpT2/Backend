from django.shortcuts import render
from .models import Question
from django.http import HttpResponse
# Create your views here.


def index(request):
    item = ["phone","car","plane"]
    return render(request,"polls/test.html", {"myitem":item})

def qlist(request):
    q_list = Question.objects.all()
    return render(request,'polls/question_list.html',{'qlist':q_list})

def detailView(request,q_id):
    q = Question.objects.get(pk = q_id)
    return render(request,"polls/detail.html",{"q":q})

def result(request,q_id):
    q = Question.objects.get(pk = q_id)
    try:
        data = request.POST['choice']
        c = q.choice_set.get(pk = data)
    except:
        return HttpResponse('Chưa chọn')
    c.vote += 1
    c.save()
    return render(request,'polls/result.html',{'q':q})
