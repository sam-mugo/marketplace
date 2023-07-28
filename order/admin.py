from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.
# admin.site.register(models.OrderItem)
# admin.site.register(models.Order)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'is_complete', 'transaction_id', 'order_total']