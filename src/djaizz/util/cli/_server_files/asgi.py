"""
ASGI config for Djaizz project.

It exposes the ASGI callable as a module-level variable named ``application``

For more information on this file, see
docs.djangoproject.com/en/dev/howto/deployment/asgi
"""


# ref: django-configurations.readthedocs.io


import os


# from django.core.asgi import get_asgi_application
from configurations.asgi import get_asgi_application


os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='settings')
os.environ.setdefault(key='DJANGO_CONFIGURATION', value='Default')


application = get_asgi_application()
