from django.urls import path

from jobsPy.blog.views import BlogPostListCreateAPIView, BlogPostRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, \
    CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('blog/', BlogPostListCreateAPIView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('blog/<int:pk>/comments/<int:comment_pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]

