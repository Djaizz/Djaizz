# Configuration file for the Sphinx documentation builder.

# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


from datetime import date
import django
import os
import sys
from recommonmark.parser import CommonMarkParser

import djai
from djai.util.config import (
    _DJAI_CONFIG_FILE_PATH_ENVVAR_NAME,
    _DJAI_CONFIG_TEMPLATE_FILE_PATH
)


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
# If the directory is relative to the documentation root,
# use os.path.abspath to make it absolute, like shown here.

os.environ[_DJAI_CONFIG_FILE_PATH_ENVVAR_NAME] = \
    _DJAI_CONFIG_TEMPLATE_FILE_PATH
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.insert(0, os.path.abspath(path='../src'))
django.setup()


# -- Project information -----------------------------------------------------

project = djai.metadata.PACKAGE
author = djai.metadata.AUTHOR
copyright = f'{date.today().year}, {author}'

# The full version, including alpha/beta/rc tags
release = djai.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*')
# or your custom ones.
extensions = [
    'sphinx.ext.autodoc',   # Include documentation from docstrings
    'sphinx.ext.autosectionlabel',   # Allow reference sections using its title
    'sphinx.ext.autosummary',   # Generate autodoc summaries

    'sphinx.ext.coverage',   # Collect doc coverage stats
    'sphinx.ext.doctest',   # Test snippets in the documentation
    'sphinx.ext.duration',   # Measure durations of Sphinx processing
    'sphinx.ext.extlinks',   # Markup to shorten external links
    'sphinx.ext.githubpages',   # Publish HTML docs in GitHub Pages
    'sphinx.ext.graphviz',   # Add Graphviz graphs
    'sphinx.ext.ifconfig',   # Include content based on configuration
    'sphinx.ext.imgconverter',   # reference image converter using Imagemagick
    'sphinx.ext.inheritance_diagram',   # Include inheritance diagrams
    'sphinx.ext.intersphinx',   # Link to other projects’ documentation
    # 'sphinx.ext.linkcode',   # Add external links to source code
    # TODO: provide linkcode_resolve function

    'sphinx.ext.imgmath',   # Render math as images
    'sphinx.ext.mathjax',   # Render math via JavaScript
    'sphinxcontrib.jsmath',   # Render math via JavaScript

    'sphinx.ext.napoleon',   # Support for NumPy and Google style docstrings
    'sphinx.ext.todo',   # Support for todo items
    'sphinx.ext.viewcode'   # Add links to highlighted source code
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory,
# that match files and directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory.
# They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# math renderer
html_math_renderer = 'mathjax'


# Source Parsers
source_parsers = {
    '.md': CommonMarkParser
}

source_suffix = '.md', '.rst'
