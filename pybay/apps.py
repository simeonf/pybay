from django.apps import AppConfig as BaseAppConfig
from django.utils.module_loading import import_module


class AppConfig(BaseAppConfig):

    name = "pybay"

    def ready(self):
        import_module("pybay\.receivers")
