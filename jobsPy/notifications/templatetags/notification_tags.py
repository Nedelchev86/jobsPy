from django import template
from jobsPy.notifications.models import NotificationJobSeeker, Notification

register = template.Library()


@register.filter
def unread_notifications(user):
    if user.is_authenticated:
        if user.jobseeker:
            return len(NotificationJobSeeker.objects.filter(user=user, is_read=False))
        else:
            return len(Notification.objects.filter(user=user))
    else:
        return 0
    