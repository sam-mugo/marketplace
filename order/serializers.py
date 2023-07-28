import uuid
from apis.serializers import ProductSerializer
from apis.permissions import IsManage, IsAdmin, IsRead
from catalog.models import Product
from rest_framework import serializers
from .models import Order, OrderItem



class OrderItemSerializer(serializers.ModelSerializer):
    item = ProductSerializer()

    class Meta: 
        model = OrderItem
        fields = ['id', 'item', 'quantity']#order
    
    def create(self, validated_data):
        item_data = validated_data.pop('item')
        order_id = validated_data.pop('order').id
        item = Product.objects.get(id=item_data.get('id'))
        # order = Order.objects.get(id=order_id)
        order_item, created = OrderItem.objects.get_or_create(item=item)#order
        # print(order_item, created)
        if not created:
            # print("Item already exists")
            order_item.quantity += 1
            order_item.save()

        order_item.order.order_total()
        return order_item

class OrderItemUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity']

    def update(self, instance, validate_data):
        instance.quantity = validate_data.get('quantity', instance.quantity)
        instance.save()
        instance.order.order_total()

        return instance.order.total


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'date_ordered', 'complete', 'transaction_id','order_items', 'total']#user
    
    def create(self, validated_data):
        print(f"validated_data: {validated_data}")
        
        user_id = validated_data.pop('user').id
        print(f"user_id: {user_id}")
        # user = User.objects.get(id=user_id)
        order = Order.objects.create()#args user=user
        return order

    def update(self, instance, validated_data):
        instance.transaction_id()
        instance.complete = True
        instance.save()

        return instance
        