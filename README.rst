sphinxcontrib.youtube
=====================

.. image:: https://img.shields.io/badge/License-BSD_3--Clause-orange.svg
    :alt: license
    :target: LICENCE
    
.. image:: https://badge.fury.io/py/sphinxcontrib-youtube.svg
    :target: https://badge.fury.io/py/sphinxcontrib-youtube
    :alt: PyPi version 

Overview
--------

This module provides support for including YouTube and Vimeo videos in Sphinx
:code:`rst` documents.

This module defines directives, :code:`youtube` and :code:`vimeo` which insert
videos from the respective platforms. They take a single, required argument,
which is the video ID: 

.. code-block:: rst 
   
   ..  youtube:: dQw4w9WgXcQ

.. code-block:: rst

   .. vimeo:: 148751763

For full usage information, please see the `web documentation
<https://sphinxcontrib-youtube.readthedocs.io>`__.
