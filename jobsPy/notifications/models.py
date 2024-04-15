from django.contrib.auth import get_user_model
from django.db import models

from jobsPy.jobs.models import Job

UserModel = get_user_model()


class Notification(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    message = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)