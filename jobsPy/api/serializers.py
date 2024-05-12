# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from jobsPy.company.models import CompanyProfile
from jobsPy.jobs.models import FavoriteJob
from jobsPy.jobseekers.models import JobSeeker

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


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'  # You can specify the fields you want to include here if needed

class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'  # You can specify the fields you want to include here if needed

class FavoriteJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteJob
        fields = '__all__'


class FavoriteStatusSerializer(serializers.Serializer):
    is_favorite = serializers.BooleanField()