from django.db import models

# Create your models here.
class SignupRecord(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    gender = models.CharField(max_length=100)
    dob = models.DateField()
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

