"""
ASGI config for DjAI project.

It exposes the ASGI callable as a module-level variable named ``application``

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi
"""


# ref: django-configurations.readthedocs.io


import os


# from django.core.asgi import get_asgi_application
from configurations.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Default')


application = get_asgi_application()
