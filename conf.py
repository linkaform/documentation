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
    'sphinx_design', #Extensión para componentes responsivos.
    'sphinxcontrib.youtube', #Extensión para incrustar videos youtube.
    'sphinxcontrib.mermaid', #Extensión que permite hacer uso de Mermaind (diagramas).
    'sphinx_copybutton', #Extensión que hace posible personalizar .. code-block::
    'sphinx.ext.graphviz', #Extensión sobre gráficos.
    'myst_parser',  #Extensión que permite a Sphinx leer MySt(Markedly Structured Text).
    'sphinx.ext.autodoc', #Automatizar la generación de documentación a partir de los comentarios y docstrings.
    #'sphinxcontrib.spelling',
    #'cards',
]
#extensions = []
source_suffix = ['.rst', '.md']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'furo'
locale_dirs = ['locale/']
gettext_compact = True 
templates_path = ['./extensions/']
html_static_path = ['static']
html_css_files = ['css/custom.css']
html_theme_options = {
    'sidebar_hide_name': True,
    'light_logo': '/img/Linkaform_light.png',
    'dark_logo': '/img/Linkaform_dark_new.png',
    'light_css_variables': {
        "color-brand-primary": "#0c1c49",
        "color-brand-content": "#2c3e50",
        "color-background-hover": "#e1e2e6",
    },
    'dark_css_variables': {
        "color-background-primary": "#1c262d", 
        "color-background-secondary": "#141b1f",
        "color-background-hover": "#27343e",
        "color-brand-primary": "#FFFFFF",
        "color-brand-content": "#E0E0E0",
        "color-header-text": "#FFFFFF",
    },
    'font-stack': "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu",
}
pygments_style = "lightbulb"
pygments_dark_style = "zenburn"
graphviz_output_format = 'png' 



