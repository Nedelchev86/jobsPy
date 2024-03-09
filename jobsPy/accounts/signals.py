
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from jobsPy.company.models import CompanyProfile
from jobsPy.jobseekers.models import JobSeeker


userModel = get_user_model()


@receiver(post_save, sender=userModel)
def create_user_profile(sender, instance, created, **kwargs):
    print(instance)
    print(instance.role)

    """
    Signal receiver function to create a user profile when a new user is created.
    """
    if created:
        if instance.role == 'jobseeker':
            JobSeeker.objects.create(user=instance)

        elif instance.role == 'company':
            CompanyProfile.objects.create(user=instance)


