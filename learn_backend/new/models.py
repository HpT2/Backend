from django.db import models
from django.utils import timezone
# Create your models here.


class posts(models.Model):
    title = models.CharField(max_length=255,blank=False,null=False)
    content = models.TextField(max_length=2000)
    Post_date = models.DateTimeField(default=timezone.now())

