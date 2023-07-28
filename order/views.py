from django.shortcuts import render
from apis.permissions import IsAdmin
from order.models import Order, OrderItem
from rest_framework.views import APIView
from rest_framework.response import Response
from order.serializers import OrderItemSerializer, OrderItemUpdateSerializer, OrderSerializer
from rest_framework import status, permissions
from rest_framework.decorators import permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class OrderItemDetailView(APIView):
    # permission_classes = (permissions.IsA)
    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    # def post(self, request):=
    #     serializer = OrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk, format=None):
        order_item = OrderItem.objects.get(id=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)


    # Returns cart
    def put(self, request, pk, format=None):
        order_item = OrderItem.objects.get(id=pk)
        serializer = OrderItemUpdateSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            cart = OrderSerializer(order_item.order).data
            # print("views line 38, Cart Total: ", order_item.order.total)
            return Response(cart, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order_item = OrderItem.objects.get(id=pk)
        order = order_item.order
        order_item.delete()
        order.order_total()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemCreateView(APIView):
    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class OrderDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    """
    List all the orders/carts of the requested user
    """
    # requires user id 
    def get(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        order = Order.objects.filter(complete=False)[0]#args user=user
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    # requires cart id 
    def put(self, request, pk, format=None):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)
    
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
