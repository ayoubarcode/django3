from django.apps import AppConfig


class ProfiloConfig(AppConfig):
    name = 'profilo'

    def ready(self):
        import profilo.signals
