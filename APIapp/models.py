from django.db import models

# Create your models here.
class books(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    lsbn=models.BigIntegerField()
    publisher=models.CharField(max_length=30)