# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

userModel = get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    password = serializers.CharField(
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )


    class Meta:
        model = userModel
        fields = ['email', 'password', 'role']  # Assuming 'role' is a field in your Account model
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }
    def create(self, validated_data):
        user = userModel.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = userModel
        fields = ['email', 'password', 'role']  # Assuming 'role' is a field in your Account model
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        user = userModel.objects.create_user(**validated_data)
        return user