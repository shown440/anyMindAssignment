from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    username = serializers.CharField(max_length=150) 
    password1 = serializers.CharField(max_length=128) 
    password2 = serializers.CharField(max_length=128) 


class UserResponseSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    username = serializers.CharField(max_length=150) 