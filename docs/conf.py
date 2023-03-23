# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import tomli
base_path = os.path.split(os.path.join(os.path.abspath(os.path.dirname(__name__))))[0]
sys.path.append(base_path)

# Reads version.py and converts to a dict of keys
version_py = {}
with open(os.path.join(base_path, 'pyats_genie_command_parse', 'version.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), version_py)

# Reads pyproject.toml and converts to python objects
with open(os.path.join(base_path, 'pyproject.toml'), 'r', encoding='utf-8') as file:
    toml = file.read()
pyproject_toml = tomli.loads(toml)

# -- Added for readthedocs.org -----------------------------------------------

master_doc = 'index'

# -- Project information -----------------------------------------------------

# The full version, including alpha/beta/rc tags
release = version_py['__version__']
project = f"{pyproject_toml['project']['name']} v{release}"
copyright = version_py['__copyright__']

# Reads authors from pyproject.toml and adds name to list
authors = []
for author_name in pyproject_toml['project']['authors']:
    authors.append(author_name.get('name'))

author = ','.join(authors)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
if html_theme == 'alabaster':
    html_theme_options = {
        'description': 'pyATS Genie, Parse Wrapper',
        'page_width': '95%',
        'body_max_width': 'auto',
        'fixed_sidebar': 'false'
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
