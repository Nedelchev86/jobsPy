from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_async_email(subject, message, recipient_list):
    send_mail(subject, message, 'your_email@example.com', recipient_list)


@shared_task
def send_password_reset_email(email, reset_url):
    subject = 'Password Reset'
    message = f'Click the following link to reset your password: {reset_url}'
    from_email = 'your@example.com'  # Replace with your email
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
