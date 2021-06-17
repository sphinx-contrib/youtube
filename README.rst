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

You can increase privacy for users of your HTML output by hiding the embedded
video behind a button. If used, connection to the video platform will be
made only if the button is clicked. You can enable this by using the "hide"
parameter. It accepts 'False' (default) or 'True' or any <string>. If a 
<string> is used then the video will be hidden and the button will show text
"Display: <string>" ::

    .. youtube:: oHg5SJYRHA0
       :hide: True
    
    .. youtube:: oHg5SJYRHA0
       :hide: Video title to show it on the button

In LaTeX output, the followinging code will be emitted for YouTube::

    \sphinxcontribyoutube{https://youtu.be/}{oHg5SJYRHA0}

The user may customise the rendering of the URL by defining this command in 
the premble. If they do not, then the default definition is used::

    \newcommand{\sphinxcontribvimeo}[2]{\begin{quote}\begin{center}\fbox{\url{#1#2}}\end{center}\end{quote}}

This prints a simple link to the video, enclosed in a box. LaTeX support for
Vimeo is similar, except that the macro is named `\sphinxcontribvimeo`.

..  -*- mode: rst; fill-column: 79 -*-
