import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'general.settings'

from django import setup
setup()

from app_models.serializers import ServerUserSerializer