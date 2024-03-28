from django.contrib.auth import get_user_model
from rest_framework import serializers

from jobsPy.blog.models import BlogPost, Comment
from jobsPy.jobseekers.models import JobSeeker


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ['id', 'first_name', 'last_name']  # Add other fields as needed


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)  # Assuming you only want to show the author's ID

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    author = JobSeekerSerializer()  # Nested serializer for JobSeeker
    comments = CommentSerializer(many=True, read_only=True)  # Nested serializer for comments

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'description', 'image_url_1', 'image_url_2', 'image_url_3', 'views', 'created_at', 'author', 'comments']

