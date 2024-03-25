from django.urls import path

from jobsPy.blog.views import BlogPostListCreateAPIView, BlogPostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('blog/', BlogPostListCreateAPIView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),
    # Other URL patterns...
]
