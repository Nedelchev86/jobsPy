from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions
from rest_framework.response import Response

from jobsPy.blog.models import BlogPost
from jobsPy.blog.permission import IsAuthor
from jobsPy.blog.serializers import BlogPostSerializer


# Create your views here.


class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthor()]
        return super().get_permissions()


class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BlogList(TemplateView):
    template_name = 'blog/blogs.html'


class SingleBlog(TemplateView):
    template_name = 'blog/single-blogs.html'



class CreateBlog(TemplateView):
    template_name = 'blog/create-blog.html'
    permission_classes = [IsAuthor()]
