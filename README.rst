sphinxcontrib.youtube
=====================

This module defines a directive, `youtube`.  It takes a single, required
argument, a YouTube video ID::

    ..  youtube:: oHg5SJYRHA0

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

A simple link to the video, enclosed in a box, will be inserted in LaTeX output.

..  -*- mode: rst; fill-column: 72 -*-
