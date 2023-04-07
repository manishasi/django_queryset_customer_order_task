from django.contrib import admin
from .models import Customers, Orders, Order_Items, Products

# Register your models here.
@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','phone_number')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=('id','customer','order_date','total_Amount')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('id','product_Name','category','description','price')

@admin.register(Order_Items)
class Order_ItemsAdmin(admin.ModelAdmin):
    list_display=('id','order','product','quantity','price')

