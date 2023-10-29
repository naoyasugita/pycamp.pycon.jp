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
# import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Python Boot Camp Text'
copyright = '2022, PyCon JP Association'
author = 'PyCon JP Association'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinxext.opengraph',
]

# コピーするときのプロンプト設定
# https://sphinx-copybutton.readthedocs.io/
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True

# https://github.com/wpilibsuite/sphinxext-opengraph
ogp_site_url = "https://pycamp.pycon.jp/"

# https://sphinxext-opengraph.readthedocs.io/en/latest/socialcards.html
ogp_social_cards = {
    "enable": True,
    "image": "images/python-boot-camp-logo.png",
    "font": "Noto Sans CJK JP",
}

# font settings for macOS and Windows
if sys.platform == "darwin":
    ogp_social_cards["font"] = "Hiragino Maru Gothic Pro"
elif sys.platform == "win32":
    ogp_social_cards["font"] = "MS PGothic"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

numfig = True

# see: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "colon_fence",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_last_updated_fmt = '%Y-%m-%d'

html_show_copyright = False

html_logo = 'images/python-boot-camp-logo.png'

html_favicon = 'images/python-boot-camp-logo.ico'

html_theme_options = {
    "source_repository": "https://github.com/pyconjp/pycamp.pycon.jp",
    "source_branch": "master",
    "source_directory": "source/",
}
