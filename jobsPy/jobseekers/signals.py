from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobSeeker


@receiver(post_save, sender=JobSeeker)
def update_jobseeker_activation(sender, instance, **kwargs):
    # Recursion
    if instance.first_name and not instance.activated:
        instance.activated = True
        instance.save()
