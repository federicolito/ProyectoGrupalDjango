from django.apps import AppConfig


class FilmhubConfig(AppConfig):
    name = 'FilmHub'
    def ready(self):
        import FilmHub.signals
