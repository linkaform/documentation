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
    'sphinx_design',
    'sphinx.ext.autodoc',
    'sphinxcontrib.youtube',
    'sphinxcontrib.mermaid', #Extensión que permite hacer uso de Mermaind
    'sphinx_copybutton',
    #'cards',
    'myst_parser',  #Extensión que permite a Sphinx leer MySt(Markedly Structured Text)
]
#extensions = []
source_suffix = ['.rst', '.md']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'press'

html_theme = 'furo'
#locale_dirs = ['./locale/']
locale_dirs = ['locale/']
gettext_compact = True 
templates_path = ['./extensions/']
html_static_path = ['static']
html_css_files = ['css/custom.css']
html_theme_options = {
    #"prefers-color-scheme": "dark
    #"primary_sidebar_end": ["index.html"],
    "relbarbgcolor": "black",
    'sidebar_hide_name': True,
    'light_logo': 'Linkaform_light.png',
    'dark_logo': 'Linkaform_dark.png',
    'light_css_variables': {
        "color-brand-primary": "#0c1c49",
        "color-brand-content": "#2c3e50",
        "font-stack": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans, Helvetica Neue ,sans-serif, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
    'dark_css_variables': {
        "color-brand-primary": "#FFFFFF",
        "color-brand-content": "#E0E0E0",
        "color-header-text": "#FFFFFF",
        "font-stack": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans, Helvetica Neue ,sans-serif, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
}
pygments_style = "lightbulb"
pygments_dark_style = "zenburn"
#html_sidebars = {"**" : 'index.html',}



