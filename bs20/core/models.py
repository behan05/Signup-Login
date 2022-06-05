from django.db import models

# Create your models here.
class SignupTB(models.Model):
    Username=models.CharField(max_length=70)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=70)
    CnfPassword=models.CharField(max_length=70)
    
