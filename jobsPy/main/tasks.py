from celery import shared_task
from django.core.mail import send_mail

from jobsPy import settings


@shared_task
def send_async_email(subject, message, recipient_list):
    sender_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender_email, recipient_list)