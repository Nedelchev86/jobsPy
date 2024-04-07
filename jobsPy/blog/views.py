from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions, pagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from jobsPy.accounts.forms import LoginForm
from jobsPy.blog.models import BlogPost, Comment
from jobsPy.blog.permission import IsAuthor
from jobsPy.blog.serializers import BlogPostSerializer, CommentSerializer, CommentSerializerCreate
from jobsPy.core.accounts_mixins import AuthorRequiredMixin


# Create your views here.
class BlogPostPagination(pagination.PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Optionally, set a maximum page size

class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostPagination
    def perform_create(self, serializer):
        # Automatically set the author as the logged-in jobseeker
        serializer.save(author=self.request.user.jobseeker)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthor()]
        return super().get_permissions()


class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthor]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BlogList(TemplateView):
    template_name = 'blog/blogs.html'


class SingleBlog(TemplateView, LoginView):
    template_name = 'blog/single-blogs.html'
    form_class = LoginForm


class CreateBlog(AuthorRequiredMixin, TemplateView):
    template_name = 'blog/create-blog.html'
    permission_classes = [IsAuthor()]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('pk')
        blog_post = BlogPost.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=blog_post)

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return CommentSerializerCreate
        return CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        # Retrieve the comment ID from the URL parameters
        comment_id = self.kwargs.get('comment_pk')

        return Comment.objects.get(pk=comment_id)


class LatestBlogPostsAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all() # Limit queryset to latest 5 blog posts
    serializer_class = BlogPostSerializer
