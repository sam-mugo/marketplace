from types import CoroutineType
import uuid
from django.db import models
from django.contrib.auth import get_user_model

from catalog.models import Product

# Create your models here.
User = get_user_model() 

class OrderItem(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name="order_items")
    # order = models.ManyToManyField(Order, related_name="order_items")
    
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    # ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    

    def __str__(self):
        return self.item.name


class Order(models.Model):
    # order_status = (
    #     ('completed', 'COMPLETED'),
    #     ('canceled', 'CANCELED'),
    #     ('abandoned', 'ABANDONED'),
    # )    

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # address = models.CharField(max_length=150)
    # city = models.CharField(max_length=50)
    # post_code = models.CharField(max_length=10)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=15)

    cart_items = models.ManyToManyField(OrderItem, related_name="order_items")
    created_at = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    order_total = models.IntegerField()

    @property
    def order_total(self):
        total = 0
        items = self.cart_items.all()

        for item in items:
            sub_total = item.item.price * item.quantity
            total += sub_total
            
            

        return total

    @property
    def transaction_id(self):
        id = str(uuid.uuid4())
        return id

        # self.order_total = total
        # self.save()


    def __str__(self) -> str:
        return f"{self.user.username}Order number is {self.transaction_id}, and the cart total is {self.order_total}"



