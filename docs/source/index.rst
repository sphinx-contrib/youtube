sphinxcontrib-youtube
=====================

Demo
----

This module provides support for including YouTube and Vimeo videos in Sphinx :code:`rst` documents.

This module defines directives, :code:`youtube` and :code:`vimeo` which insert videos from the respective platforms. They take a single, required argument, wich is the video ID:

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ

..  youtube:: dQw4w9WgXcQ
   :align: center
   :aspect: 16:9

.. code-block:: rst

   .. vimeo:: 148751763

.. vimeo:: 148751763
   :align: center
   :aspect: 16:9

Usage
-----

The referenced video will be embedded into HTML and Latex outputs, the behaviour will be slightly different for obvious reasons.

HTML
^^^^

By default, the embedded video will be sized for 720p content. To control this, the parameters :code:`aspect`, :code:`width`, and :code:`height` may optionally be provided:

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

For YouTube "privacy mode", use the directive option :privacy_mode: (and for vimeo, :url_parameters: ?dnt=1):

.. code-block:: rst

   ..  youtube:: dQw4w9WgXcQ
      :privacy_mode:

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

The user may customise the rendering of the URL by defining this command in the preamble. The captions will be downloaded to the latex folder and can thus be used as images in the :code:`.pdf` document. We are using the `Vumbnail <https://vumbnail.com>`__ (vimeo) and `get-youtube-thumbnail <https://www.get-youtube-thumbnail.com>`__ (youtube) web services to retrieve them. Here is an example of custom command for both the vimeo and the yoututbe output. This needs to be added in the :code:`conf.py` file:

.. code-block:: python

   # conf.py
   # ...
   # -- Option for Latex output ---------------------------------------------------

   # create a custom sphinx output for the youtube and vimeo video
   youtube_cmd = r"\newcommand{\sphinxcontribyoutube}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}" + "\n"
   vimeo_cmd = r"\newcommand{\sphinxcontribvimeo}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}" + "\n"

   latex_elements = {"preamble": youtube_cmd + vimeo_cmd}

This example will show the video as a figure using the thumbnail as image and the url as caption (clickable link). This is the one we use for this very documentation. remember that the argument of your command are the following:

-   :code:`#1`: the platform url
-   :code:`#2`: the video ID (it's also the name of the image: :code:`#2.jpg`
-   :code:`#3`: the options of the url

If no custom command is set in :code:`conf.py`, then the default definition is used:

.. code-block:: latex

    \newcommand{\sphinxcontribyoutube}[3]{\begin{quote}\begin{center}\fbox{\url{#1#2#3}}\end{center}\end{quote}}

This prints a simple link to the video, enclosed in a box. LaTeX support for Vimeo is similar, except that the macro is named :code:`\sphinxcontribvimeo`.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
