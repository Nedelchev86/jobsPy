from rest_framework import serializers

from jobsPy.blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'description', 'image_url_1', 'image_url_2']