from django.urls import path
from .views import CategoryApiView, OrderApiView, ProductApiView

urlpatterns = [
    path('api/categories', CategoryApiView.as_view(), name='category_list'),
    path('api/products', ProductApiView.as_view(), name='product_list'),
    path('api/orders', OrderApiView.as_view(), name='order_list'),
]