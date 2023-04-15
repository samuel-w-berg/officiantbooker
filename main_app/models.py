from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.

class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    date = models.DateField('Wedding Date: ')

