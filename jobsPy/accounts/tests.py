from django.test import TestCase

# Create your tests here.
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_async_email(subject, message, recipient_list):
    send_mail(subject, message, 'your_email@example.com', recipient_list)