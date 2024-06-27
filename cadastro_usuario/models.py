from django.db import models

# Create your models here.

class Usuario(models.Model):
    nickname = models.CharField(primary_key=True, max_length=155, default='')
    name = models.CharField(max_length=155, default='')
    email = models.EmailField(max_length=254, default='')
    age = models.IntegerField(default=0)
    senha = models.CharField(max_length=155, default='')

    
