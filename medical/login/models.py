from django.db import models
from django import forms
from .models import *
# Create your models here.

class Register(models.Model):
    firstname=models.CharField(max_length=1000,blank=True)
    lastname=models.CharField(max_length=2000,blank=True)
    Profilepicture=models.ImageField(null=False,upload_to="uploads/",blank=True)
    username=models.CharField(max_length=2000,blank=True)
    email=models.EmailField(blank=True)
    password=models.CharField(max_length=2000,blank=True)
    confirmpassword=models.CharField(max_length=2000,blank=True)
    address_line=models.CharField(max_length=2000,blank=True)
    address_city=models.CharField(max_length=2000,blank=True)
    address_state=models.CharField(max_length=2000,blank=True)
    address_pincode=models.CharField(max_length=2000,blank=True)
    status=models.CharField(max_length=1,default="1")
  
    
   
 