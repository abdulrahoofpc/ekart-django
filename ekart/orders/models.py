from django.db import models
from products.models import Product
from customers.models import Customer
# from orders.models import Order


class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),((DELETE,'Delete')))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=(
        (ORDER_PROCESSED,'ORDER_PROCESSED'),
        (ORDER_DELIVERED,'ORDER_DELIVERED'),
        (ORDER_REJECTED,'ORDER_REJECTED')
    )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delet_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

class orderItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')


