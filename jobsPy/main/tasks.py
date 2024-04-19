from celery import shared_task
from django.core.mail import send_mail
from jobsPy import settings
from jobsPy.main.models import Subscriber


# @shared_task
def send_contact_form_confirmation(name, email):
    subject = 'Confirmation: Your Message has been Received'
    message = (f'Hi {name},\n\nThank you for contacting us. We have received'
               f' your message and will get back to you as soon as possible.\n\nBest regards,\nJobsPy Team')
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)


# @shared_task
def send_contact_form_notification_to_team(name, email, subject, phone, message):
    # Construct email subject and message
    email_subject = 'New Contact Form Submission'
    email_message = (f'A new contact form has been submitted:\n\nName: {name}\n'
                     f'Email: {email}\nSubject: {subject}\nPhone: {phone}\nMessage: {message}')

    # Set sender and recipient email addresses
    from_email = settings.EMAIL_HOST_USER
    admin_email = settings.EMAIL_HOST_USER

    # Send the email notification
    send_mail(email_subject, email_message, from_email, [admin_email])


@shared_task
def send_news_notification(news_title, news_content):
    subscribers = Subscriber.objects.filter(is_active=True)
    subject = f"{news_title} - JobsPy"
    message = f"{news_content}\n\nRegards,\nJobsPy Team"
    recipient_list = [subscriber.email for subscriber in subscribers]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
