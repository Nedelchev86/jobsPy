from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobsPy.accounts'

    def ready(self):
        import jobsPy.accounts.signals