from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Seller(models.Model):
    seller_image = models.ImageField(upload_to = 'image/',null = True)
    product = models.TextField()
    phone_number = models.CharField(max_length = 10,blank =False)
class Buyer(models.Model):
    buyer_name = models.TextField()
    buyer_location = models.TextField()
    product = models.TextField()
    phone_number = models.CharField(max_length = 10,blank =False)
