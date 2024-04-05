import importlib
from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smuull.post'

    def ready(self):
        importlib.import_module('smuull.post.signals')