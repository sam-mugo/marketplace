from unicodedata import category
from rest_framework import generics, status, filters
# from rest_framework import filters as fl
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#from ..catalog.models import Order
from . import model_filters
from catalog.models import Category, Subcategory, Product, Order, OrderItem
from .serializers import CategorySerializer
from .serializers import SubcategorySerializer
from .serializers import ProductSerializer
from .serializers import OrderSerializer


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #result = Product.objects.values('category_id').annotate(count=Count('category_id'))
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubcategoryApiView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def post(self, request):
        serializer = SubcategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'category_id', 'subcategory_id']
    search_fields = ['name']
    ordering_fileds = ['id', 'price']
    
    def get_queryset(self):
        category_id = self.request.query_params.get('category_id', '')
        if category_id:
            return Product.objects.filter(category_id=category_id)
        return Product.objects.all()

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
