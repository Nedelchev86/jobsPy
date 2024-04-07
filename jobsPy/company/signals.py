from django.db.models.signals import post_save
from django.dispatch import receiver

from jobsPy.company.models import CompanyProfile


@receiver(post_save, sender=CompanyProfile)
def update_company_activation(sender, instance, **kwargs):
    # Recursion
    if instance.name and not instance.activated:
        instance.activated = True
        instance.save()
