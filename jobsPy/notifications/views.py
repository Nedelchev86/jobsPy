from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from jobsPy.notifications.models import NotificationJobSeeker


class NotificationListView(LoginRequiredMixin, ListView):
    model = NotificationJobSeeker
    template_name = 'notifications/notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        print(self.request.user)
        print(self)
        return super().get_queryset().filter(user=self.request.user)
