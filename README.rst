sphinxcontrib.youtube
=====================

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

A simple link to the video, enclosed in a box, will be inserted in LaTeX output.

..  -*- mode: rst; fill-column: 72 -*-
