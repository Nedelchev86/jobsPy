from django.db.models.signals import post_save
from django.dispatch import receiver
from jobsPy.jobs.models import Applicant
from jobsPy.notifications.models import Notification, NotificationJobSeeker


@receiver(post_save, sender=Applicant)
def create_notification(sender, instance, created, **kwargs):
    if created:
        job_owner = instance.job.user
        message = f" has applied for the job: "
        Notification.objects.create(user=job_owner, job=instance.job, job_seeker=instance.user,  message=message)
    else:
        NotificationJobSeeker.objects.create(
            user=instance.user,
            job=instance.job,
            status=instance.get_status(),
            comment=instance.comment,

        )