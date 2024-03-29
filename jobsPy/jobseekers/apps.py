from django.apps import AppConfig


class JobseekersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobsPy.jobseekers'

    def ready(self):
        import jobsPy.jobseekers.signals
