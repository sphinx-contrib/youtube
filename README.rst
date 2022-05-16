sphinxcontrib.youtube
=====================

.. image:: https://img.shields.io/badge/License-BSD_3--Clause-orange.svg
    :alt: license
    :target: LICENCE
    
.. image:: https://badge.fury.io/py/sphinxcontrib-youtube.svg
    :target: https://badge.fury.io/py/sphinxcontrib-youtube
    :alt: PyPi version 

This module provides support for including YouTube and Vimeo videos
in Sphinx rst documents.

This module defines directives, `youtube` and `vimeo` which insert videos
from the respective platforms. They take a single, required argument, a 
YouTube video ID::

    ..  youtube:: oHg5SJYRHA0

or a Vimeo video ID::

    .. vimeo:: 486106801

The referenced video will be embedded into HTML output.  By default, the
embedded video will be sized for 720p content.  To control this, the
parameters "aspect", "width", and "height" may optionally be provided::

    ..  youtube:: oHg5SJYRHA0
        :width: 640
        :height: 480

    ..  youtube:: oHg5SJYRHA0
        :aspect: 4:3

    ..  youtube:: oHg5SJYRHA0
        :width: 100%

    ..  youtube:: oHg5SJYRHA0
        :height: 200px

To set the alignment of the embedded video's iframe in the HTML output, an 
optional "align" parameter can be specified, similar to the rst :image: 
directive::

    ..  youtube:: oHg5SJYRHA0
        :align: center

To start the video at a specific time the parameter "url_parameters" may be used
(quotes required for Vimeo videos)::

    ..  youtube:: oHg5SJYRHA0
        :url_parameters: ?start=300

    .. vimeo:: 73214621
        :url_parameters: "#t=3m13s"

For YouTube "privacy mode", use the directive option
``:privacy_mode:`` (and for vimeo, ``:url_parameters: ?dnt=1``)::

    ..  youtube:: oHg5SJYRHA0
        :privacy_mode:

In LaTeX output, the following code will be emitted for YouTube::

    \sphinxcontribyoutube{https://youtu.be/}{oHg5SJYRHA0}{?start=300}

The user may customise the rendering of the URL by defining this command in 
the premble. If they do not, then the default definition is used::

    \newcommand{\sphinxcontribyoutube}[3]{\begin{quote}\begin{center}\fbox{\url{#1#2#3}}\end{center}\end{quote}}

This prints a simple link to the video, enclosed in a box. LaTeX support for
Vimeo is similar, except that the macro is named `\sphinxcontribvimeo`.

**Note:** The third argument to this macro was introduced in version 1.1. Prior
to this only the first two arguments were passed.

..  -*- mode: rst; fill-column: 79 -*-
