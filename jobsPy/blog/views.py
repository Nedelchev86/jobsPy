from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics

from jobsPy.blog.models import BlogPost
from jobsPy.blog.serializers import BlogPostSerializer


# Create your views here.


class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogList(TemplateView):
    template_name = 'blog/blogs.html'
