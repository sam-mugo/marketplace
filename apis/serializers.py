# import uuid
from rest_framework import serializers
from catalog.models import Category, Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'description', 'image_url', 'category_id')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category_id', 'id', 'name', 'description', 'price', 'stock', 'image_url')




class OrderItemsSerialier(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')
