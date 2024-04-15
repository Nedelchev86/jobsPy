from django.urls import path

from jobsPy.notifications.views import NotificationListView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
]
