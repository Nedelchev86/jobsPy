from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Seniority(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = RichTextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CompanySubscription(models.Model):
    job_seeker = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="subscriptions")
    company = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="subscribers")
