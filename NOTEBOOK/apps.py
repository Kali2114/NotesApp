from django.apps import AppConfig


class NotebookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NOTEBOOK'

    def ready(self):
        from . import signals
