"""Djaizz Data Module Config."""


from sys import version_info

from django.apps.config import AppConfig

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('DjaizzDataModuleConfig',)


# docs.djangoproject.com/en/dev/ref/applications/#application-configuration
class DjaizzDataModuleConfig(AppConfig):
    """Djaizz Data Module Config."""

    # AppConfig.name
    # Full Python path to the application, e.g. 'django.contrib.admin'.
    # This attribute defines which application the configuration applies to.
    # It must be set in all AppConfig subclasses.
    # It must be unique across a Django project.
    name: str = 'djaizz.data'

    # AppConfig.label
    # Short name for the application, e.g. 'admin'
    # This attribute allows relabeling an application
    # when two applications have conflicting labels.
    # It defaults to the last component of name.
    # It should be a valid Python identifier.
    # It must be unique across a Django project.
    label: str = 'AIData'

    # AppConfig.verbose_name
    # Human-readable name for the application, e.g. “Administration”.
    # This attribute defaults to label.title().
    verbose_name: str = 'Djaizz: Data'

    # AppConfig.path
    # Filesystem path to the application directory,
    # e.g. '/usr/lib/pythonX.Y/dist-packages/django/contrib/admin'.
    # In most cases, Django can automatically detect and set this,
    # but you can also provide an explicit override as a class attribute
    # on your AppConfig subclass.
    # In a few situations this is required; for instance
    # if the app package is a namespace package with multiple paths.
    # path: str = ...

    # AppConfig.default
    # Set this attribute to False
    # to prevent Django from selecting a configuration class automatically.
    # This is useful when apps.py defines only one AppConfig subclass
    # but you don’t want Django to use it by default.
    # Set this attribute to True
    # to tell Django to select a configuration class automatically.
    # This is useful when apps.py defines more than one AppConfig subclass
    # and you want Django to use one of them by default.
    # By default, this attribute isn’t set.
    default: bool = True

    # AppConfig.default_auto_field
    # The implicit primary key type to add to models within this app.
    # You can use this to keep AutoField
    # as the primary key type for third party applications.
    # By default, this is the value of DEFAULT_AUTO_FIELD.
    default_auto_field: str = 'django.db.models.fields.AutoField'

    def ready(self) -> None:
        """Run tasks to initialize module."""
