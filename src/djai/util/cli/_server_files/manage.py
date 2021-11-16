#!/usr/bin/env python3


"""Django administration/management script."""


# ref: django-configurations.readthedocs.io


import os
import sys

from configurations.management import execute_from_command_line


if __name__ == '__main__':
    os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='settings')
    os.environ.setdefault(key='DJANGO_CONFIGURATION', value='Default')

    execute_from_command_line(argv=sys.argv)
