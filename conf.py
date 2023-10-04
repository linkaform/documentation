import sys
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LinkaForm'
copyright = '2023, LinkaForm'
author = 'LinkaForm'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []

language = 'es'
languages_names = {
    'en': 'EN',
    'es': 'ES',
    'fr': 'FR',
}

extension_dir = Path('extensions')
sys.path.insert(0, str(extension_dir.absolute()))
extensions = [
    'sphinxcontrib.mermaid', #Extensión que permite hacer uso de Mermaind
    'cards',
    'myst_parser',  #Extensión que permite a Sphinx leer MySt(Markedly Structured Text)
]
#extensions = []
source_suffix = ['.rst', '.md']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'press'
html_theme = 'furo'
html_static_path = ['_static']
locale_dirs = ['./locale/']
templates_path = ['./extensions/']
html_css_files = ['custom.css']
html_logo = '_static/LogotipoAzul.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    "rightsidebar": "true",
    "relbarbgcolor": "pink",
}

