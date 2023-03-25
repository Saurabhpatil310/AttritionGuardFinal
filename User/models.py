from django.db import models

# Create your models here.

class Register(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    moblie=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
