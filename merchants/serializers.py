from rest_framework import serializers
from .models import Merchant
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class RegisterMerchantSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = Merchant
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages
            )
        return attrs

    def create(self, validated_data):
        return Merchant.objects.create_user(**validated_data)

class MerchantLoginSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access'],
        }
    
    class Meta:
        model = Merchant
        fields = ['password', 'username', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Account disabled contact admin')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }


class MerchantLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')