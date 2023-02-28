"""
WSGI config for Djaizz project.

It exposes the WSGI callable as a module-level variable named ``application``

For more information on this file, see
docs.djangoproject.com/en/dev/howto/deployment/wsgi
"""


# ref: django-configurations.readthedocs.io


import os

# from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application


os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='settings')
os.environ.setdefault(key='DJANGO_CONFIGURATION', value='Default')


application = get_wsgi_application()
