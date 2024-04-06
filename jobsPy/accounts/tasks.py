from django.test import TestCase

# Create your tests here.
from celery import shared_task
from django.core.mail import send_mail

from jobsPy import settings
