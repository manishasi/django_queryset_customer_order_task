from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Customers(models.Model):
    first_name = models.CharField(max_length=255,default=None,null=True,blank=True)
    last_name = models.CharField(max_length=255,default=None,null=True,blank=True)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_date =  models.DateField(auto_now=False, auto_now_add=False)
    total_Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Customer: {self.customer} - Total Amount: {self.total_Amount}"

class Products(models.Model):
    product_Name = models.CharField( max_length=255)
    category = models.CharField( max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.product_Name

class Order_Items(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='pro')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order: {self.order} - Product: {self.product}"
