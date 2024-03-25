from django.urls import path

from jobsPy.blog.views import BlogPostListCreateAPIView, BlogPostRetrieveUpdateDestroyAPIView, BlogList

urlpatterns = [
    path('blog/', BlogPostListCreateAPIView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    # Other URL patterns...
]
