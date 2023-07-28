from django.urls import path
from .views import CategoryApiView, CategoryCreateApiView, ProductListApiView, ProductByCategory, RetrieveUpdateProduct, ProductCreateApiView

urlpatterns = [
    path('api/categories', CategoryApiView.as_view(), name='category_list'),
    path('api/category', CategoryCreateApiView.as_view(), name='category_add'),
    path('api/category', CategoryCreateApiView.as_view(), name='category_add'),
    path('api/products', ProductListApiView.as_view(), name='product_list'),
    path('api/product', ProductCreateApiView.as_view(), name='product_add'),
    path('api/products/<pk>/', RetrieveUpdateProduct.as_view(), name='product_patch'),
    path('api/products/category/<str:query>/', ProductByCategory.as_view(), name='products_bycategory'),
    # path('api/orders', OrderApiView.as_view(), name='order_list'),
]