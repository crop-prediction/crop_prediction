from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40,primary_key=True)
    password=models.CharField(max_length=40)
    gender=models.CharField(max_length=40)
    dob=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
