from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    seller_image = models.ImageField(upload_to = 'image/',null = True)
    product = models.TextField()
    phone_number = models.CharField(max_length = 10,blank =False)
class Buyer(models.Model):
    buyer_name = models.TextField()
    buyer_location = models.TextField()
    product = models.TextField()
    phone_number = models.CharField(max_length = 10,blank =False)
class Product(models.Model):
    product_image = models.ImageField(upload_to = 'image/',null = True)
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length = 10)
    
