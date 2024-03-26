from django.urls import path

from jobsPy.blog.views import BlogList, SingleBlog, CreateBlog

urlpatterns = [
    # path('blog/', BlogPostListCreateAPIView.as_view(), name='blog-list'),
    # path('blog/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),
    path('', BlogList.as_view(), name='blog-list'),
    path('<int:pk>/', SingleBlog.as_view(), name='blog-detail'),
    path('add/', CreateBlog.as_view(), name='blog-create'),
    # Other URL patterns...
]
