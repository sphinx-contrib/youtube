"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""


# -- Path setup ----------------------------------------------------------------

from datetime import datetime

from sphinxcontrib.youtube import __version__

# -- Project information -------------------------------------------------------

project = "sphinxcontrib-youtube"
author = "David A. Ham, Chris Pickel and others"
copyright = f"2011-{datetime.now().year}, {author}"
release = __version__

# -- General configuration -----------------------------------------------------

extensions = ["sphinx_copybutton", "sphinxcontrib.youtube", "sphinx_design"]
templates_path = ["_templates"]
exclude_patterns = ["**.ipynb_checkpoints"]

# -- Options for HTML output ---------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "logo": {
        "text": project,
    },
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sphinx-contrib/youtube",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/sphinxcontrib-youtube/",
            "icon": "fa-brands fa-python",
        },
    ],
}
html_context = {
    "github_user": "sphinx-contrib",
    "github_repo": "youtube",
    "github_version": "main",
    "doc_path": "docs",
}

# -- Option for Latex output ---------------------------------------------------

# create a custom sphinx output for the youtube, vimeo and peertube video
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

peertube_cmd = (
    r"\newcommand{\sphinxcontribpeertube}[3]"
    r"{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    "\n"
)

latex_elements = {"preamble": youtube_cmd + vimeo_cmd + peertube_cmd}
