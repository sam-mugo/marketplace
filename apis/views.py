# from apis.permissions import IsManage
from rest_framework import generics, status, filters, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators.cache import cache_page
from catalog.models import Category, Product
from .serializers import CategorySerializer
# from .serializers import OrderItemUpdateSerializer
from .serializers import ProductSerializer
from .decorators import validate_request_data
# from django.utils.decorators import method_decorator
# from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from .permissions import IsAdmin, IsManage, IsRead

class CategoryApiView(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny, IsRead)
    
    result = Product.objects.values('category_id').annotate(count=Count('category_id'))
    
    
class CategoryCreateApiView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsManage)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryPatchView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsManage,)



class ProductListApiView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'category_id']
    search_fields = ['name']
    ordering_fileds = ['id', 'price']
    
    def get_queryset(self):
        category_id = self.request.query_params.get('category_id', '')
        if category_id:
            return Product.objects.filter(category_id=category_id)
        return Product.objects.all()

    

class ProductCreateApiView(generics.CreateAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, IsManage,)
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'category_id']
    search_fields = ['name']
    ordering_fileds = ['id', 'price']

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateProduct(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsAdmin,)

class ProductByCategory(APIView):

    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, query):
        queryset = Product.objects.filter(category_id=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)