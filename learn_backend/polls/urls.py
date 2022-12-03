from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index,name = 'poll'),
    path('qlist/',views.qlist, name = 'qlist'),
    path('detail/<int:q_id>',views.detailView,name = 'detail'),
    path('result/<int:q_id>',views.result, name = 'result'),
]