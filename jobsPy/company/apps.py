from django.apps import AppConfig


class CompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobsPy.company'

    def ready(self):
        import jobsPy.company.signals

