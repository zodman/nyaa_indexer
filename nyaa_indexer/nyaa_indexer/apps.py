from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "nyaa_indexer"

    def ready(self):
        import_module("nyaa_indexer.receivers")
