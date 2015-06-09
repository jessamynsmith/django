from django.apps import apps
from django.db.models import signals
from django.contrib.contenttypes.management import update_contenttypes

def remove_contenttypes(app):
    for app_config in apps.get_app_configs():
        if app_config.name == app:
            update_contenttypes(app_config, force_remove=True)
