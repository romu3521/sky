from django.apps import AppConfig


class BasecomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basecom'

    def ready(self):
        try:
            import basecom.signals
        except ImportError as e:
            print(e)
