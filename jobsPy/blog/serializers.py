from django.contrib.auth import get_user_model
from rest_framework import serializers

from jobsPy.blog.models import BlogPost
from jobsPy.jobseekers.models import JobSeeker


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['id', 'first_name', 'last_name']  # Add other fields as needed


class BlogPostSerializer(serializers.ModelSerializer):
    author = JobSeekerSerializer()  # Nested serializer for JobSeeker
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'description', 'image_url_1', 'image_url_2', 'image_url_3', 'views', 'created_at', 'author']
