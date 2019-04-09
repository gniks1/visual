from django.db import models

# Create your models here.
class abc(models.Model):
    ename= models.CharField(max_length=64)
    eno= models.IntegerField()
    esal=models.FloatField()
