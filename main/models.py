import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

class Entry(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateField(default=timezone.now)
    amount = models.FloatField(default=0)
    description = models.TextField()
    isIncome = models.BooleanField()
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)