# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup ----------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime

from sphinxcontrib.youtube import __version__

# -- Project information -------------------------------------------------------

project = "sphinxcontrib-youtube"
author = "David A. Ham, Chris Pickel and others"
copyright = f"2011-{datetime.now().year}, {author}"

# The full version, including alpha/beta/rc tags
release = __version__

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_copybutton", "sphinxcontrib.youtube"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**.ipynb_checkpoints"]


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]


# -- Option for Latex output ---------------------------------------------------

# create a custom sphinx output for the youtube and vimeo video
youtube_cmd = (
    r"\newcommand{\sphinxcontribyoutube}[3]"
    r"{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    "\n"
)
vimeo_cmd = (
    r"\newcommand{\sphinxcontribvimeo}[3]"
    r"{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    "\n"
)

latex_elements = {"preamble": youtube_cmd + vimeo_cmd}
