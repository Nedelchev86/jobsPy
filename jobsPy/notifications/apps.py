from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobsPy.notifications'

    def ready(self):
        import jobsPy.notifications.signals