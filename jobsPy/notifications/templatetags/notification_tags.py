from django import template
from jobsPy.notifications.models import NotificationJobSeeker, Notification

register = template.Library()


@register.filter
def unread_notifications(user):
    if user.role == "jobseeker":
            return len(NotificationJobSeeker.objects.filter(user=user, is_read=False))
    elif user.role == "company":
            return len(Notification.objects.filter(user=user, is_read=False))
    else:
        return 0
    