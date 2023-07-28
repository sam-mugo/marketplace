from django.urls import path

from .views import OrderDetailView, OrderCreateView ,OrderItemDetailView, OrderItemCreateView


urlpatterns = [
    path("orders/<int:pk>/", OrderDetailView.as_view()),
    path("order/create/", OrderCreateView.as_view()),
    path("order_item/<int:pk>/", OrderItemDetailView.as_view()),
    path("order_item/add/", OrderItemCreateView.as_view()),
]
