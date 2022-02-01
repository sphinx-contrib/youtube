sphinxcontrib-youtube
=====================

Demo
----

This module provides support for including YouTube and Vimeo videos in Sphinx rst documents.

This module defines directives, code:`youtube` and :code:`vimeo` which insert videos from the respective platforms. They take a single, required argument, wich is the video ID: 

.. code-block:: rst 
   
   ..  youtube:: dQw4w9WgXcQ

.. code-block:: rst

   .. vimeo:: 148751763

.. vimeo:: 148751763

Usage
-----

HTML
^^^^

The referenced video will be embedded into HTML and Latex outputs.  By default, the embedded video will be sized for 720p content. To control this, the
parameters :code:`aspect`, :code:`width`, and :code:`height` may optionally be provided:

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :width: 640
      :height: 480

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :aspect: 4:3

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :width: 100%

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :height: 200px

To set the alignment of the embedded video's iframe in the HTML output, an optional :code:`align` parameter can be specified, similar to the rst :code:`image` directive:

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :align: center

To start the video at a specific time the parameter "url_parameters" may be used (quotes required for Vimeo videos):

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :url_parameters: ?start=43

.. code-block:: rst

   .. vimeo:: 148751763
      :url_parameters: "#t=0m43s"

Latex
^^^^^

In LaTeX output, the following code will be emitted for the videos:

.. code-block:: latex

   \sphinxcontribyoutube{https://youtu.be/}{dQw4w9WgXcQ}{?start=43}

.. code-block:: latex

   \sphinxcontribvimeo{https://player.vimeo.com/video/}{148751763}{"#t=0m43s"}

The user may customise the rendering of the URL by defining this command in the preamble. If they do not, then the default definition is used:

.. code-block:: latex

    \newcommand{\sphinxcontribyoutube}[3]{\begin{quote}\begin{center}\fbox{\url{#1#2#3}}\end{center}\end{quote}}

This prints a simple link to the video, enclosed in a box. LaTeX support for Vimeo is similar, except that the macro is named :code:`\sphinxcontribvimeo`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
