from django.contrib.auth import get_user_model
from django.db import models

from jobsPy.jobseekers.models import JobSeeker

userModel = get_user_model()

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=2000, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    more_info = models.TextField(null=False, blank=False)
    image_url_1 = models.URLField(null=False, blank=False)
    image_url_2 = models.URLField(null=False, blank=False)
    image_url_3 = models.URLField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(userModel, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)