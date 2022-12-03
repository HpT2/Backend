from django.db import models

# Create your models here.
class Question(models.Model):
    qtest = models.CharField(max_length=200)
    time = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    context = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)