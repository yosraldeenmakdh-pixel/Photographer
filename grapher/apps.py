from django.apps import AppConfig


class GrapherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grapher'

    def ready(self):
        import grapher.signals
