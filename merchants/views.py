from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterMerchantSerializers, MerchantLoginSerializers, MerchantLogoutSerializer

class MerchantRegisterView(generics.GenericAPIView):
    serializer_class = RegisterMerchantSerializers
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class MerchantLoginAPIView(generics.GenericAPIView):
    serializer_class = MerchantLoginSerializers
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MerchantLogoutAPIView(generics.GenericAPIView):
    serializer_class = MerchantLogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)