#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from .utils import get_size, css
from .youtube import depart_youtube_node

CONTROL_HEIGHT = 30

class vimeo(nodes.General, nodes.Element): pass

def visit_vimeo_node(self, node):
    aspect = node["aspect"]
    width = node["width"]
    height = node["height"]

    if aspect is None:
        aspect = 16, 9

    div_style = {}
    if (height is None) and (width is not None) and (width[1] == "%"):
        div_style = {
            "padding-top": "%dpx" % CONTROL_HEIGHT,
            "padding-bottom": "%f%%" % (width[0] * aspect[1] / aspect[0]),
            "width": "%d%s" % width,
            "position": "relative",
        }
        style = {
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "border": "0",
        }
        attrs = {
            "src": "https://player.vimeo.com/video/%s" % node["id"],
            "style": css(style),
        }
    else:
        if width is None:
            if height is None:
                width = 560, "px"
            else:
                width = height[0] * aspect[0] / aspect[1], "px"
        if height is None:
            height = width[0] * aspect[1] / aspect[0], "px"
        style = {
            "width": "%d%s" % width,
            "height": "%d%s" % (height[0] + CONTROL_HEIGHT, height[1]),
            "border": "0",
        }
        attrs = {
            "src": "https://player.vimeo.com/video/%s" % node["id"],
            "style": css(style),
        }
    attrs["allowfullscreen"] = "true"
    div_attrs = {
        "CLASS": "vimeo_wrapper",
        "style": css(div_style),
    }
    self.body.append(self.starttag(node, "div", **div_attrs))
    self.body.append(self.starttag(node, "iframe", **attrs))
    self.body.append("</iframe></div>")

def visit_vimeo_node_latex(self,node):
    self.body.append(r'\begin{quote}\begin{center}\fbox{\url{https://player.vimeo.com/video/%s}}\end{center}\end{quote}'%node['id'])


class Vimeo(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
    }

    def run(self):
        if "aspect" in self.options:
            aspect = self.options.get("aspect")
            m = re.match("(\d+):(\d+)", aspect)
            if m is None:
                raise ValueError("invalid aspect ratio %r" % aspect)
            aspect = tuple(int(x) for x in m.groups())
        else:
            aspect = None
        width = get_size(self.options, "width")
        height = get_size(self.options, "height")
        return [vimeo(id=self.arguments[0], aspect=aspect, width=width, height=height)]


def unsupported_visit_vimeo(self, node):
    self.builder.warn('vimeo: unsupported output format (node skipped)')
    raise nodes.SkipNode


_NODE_VISITORS = {
    'html': (visit_vimeo_node, depart_youtube_node),
    'latex': (visit_vimeo_node_latex, depart_youtube_node),
    'man': (unsupported_visit_vimeo, None),
    'texinfo': (unsupported_visit_vimeo, None),
    'text': (unsupported_visit_vimeo, None)
}


def setup(app):
    app.add_node(vimeo, **_NODE_VISITORS)
    app.add_directive("vimeo", vimeo)
