"""Set up DjAI package in editable mode for local development."""


# setuptools.pypa.io/en/latest/userguide/quickstart.html?highlight=editable#development-mode


from setuptools import setup


setup(name='DjAI',
      version='0.0.0.dev0',
      packages=['djai'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      namespace_packages=[])
