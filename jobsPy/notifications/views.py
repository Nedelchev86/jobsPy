from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from jobsPy.notifications.models import Notification


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
