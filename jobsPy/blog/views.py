from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from jobsPy.blog.models import BlogPost, Comment
from jobsPy.blog.permission import IsAuthor
from jobsPy.blog.serializers import BlogPostSerializer, CommentSerializer


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


class CommentListCreateAPIView(generics.CreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the post ID from the URL parameters
        post_id = self.kwargs.get('pk')
        # Filter comments based on the specified post ID
        print(post_id)
        return Comment.objects.filter(pk=post_id)

    def perform_create(self, serializer):
        # Retrieve the post ID from the URL parameters
        post_id = self.kwargs.get('pk')
        # Retrieve the blog post object based on the post ID
        blog_post = BlogPost.objects.get(pk=post_id)
        # Set the post field of the comment to the blog post object
        serializer.save(author=self.request.user, post=blog_post)
        serializer.save(author=self.request.user)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer