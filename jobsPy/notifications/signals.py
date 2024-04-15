from django.db.models.signals import post_save
from django.dispatch import receiver
from jobsPy.jobs.models import Applicant
from jobsPy.notifications.models import Notification


@receiver(post_save, sender=Applicant)
def create_notification(sender, instance, created, **kwargs):
    if created:
        job_owner = instance.job.user
        message = f"{instance.user.jobseeker} has applied for the job: {instance.job.title}"
        Notification.objects.create(user=job_owner, job=instance.job, message=message)