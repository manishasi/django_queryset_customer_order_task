from django.shortcuts import render
from .models import Customers, Orders, Order_Items, Products
# Create your views here.
# def customers(request):
#     customers = Customers.objects.prefetch_related('orders_set__items__product').get(id=1)
#     for order in customers.orders_set.all():
#         print("bshdbdkjsbdkj",order)
#         for item in order.items.all():
#             print(item.product.category)
#             print(item.quantity)
        
def customers(request):
        customers = Customers.objects.prefetch_related('orders_set__items__product')

        for customer in customers:
            print("Customer Name:", customer.first_name, customer.last_name)
            print("Email Address:", customer.email)
            print("Phone Number:", customer.phone_number)
            for order in customer.orders_set.all():
                print("Order Date:", order.order_date)
                print("Total Amount:", order.total_Amount)
                for item in order.items.all():
                        print("Product Name:", item.product.product_Name)
                        print("Category:", item.product.category)
                        print("Description:", item.product.description)
                        print("Price:", item.price)
                        print("Quantity:", item.quantity)
            print("\n")
    # orders = Orders.objects.filter(customer=customer_ID).select_related('orders').prefetch_related('Order_Items_set__Products')
    # print("SQLquery:",products.query)
        print(customers,"customers...........................")
        context = {
            'customers': customers,
        }

        return render(request, 'customer_orders.html', context)