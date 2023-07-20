"""Directive dedicated to the peertube platform."""

from docutils.parsers.rst import directives

from . import utils

# https://docs.joinpeertube.org/api/embed-player


class peertube(utils.video):
    """Empty video node class."""

    pass


class PeerTube(utils.Video):
    """Custom version of the Video Directive."""

    _node = peertube
    _thumbnail_url = ""
    _platform = "PeerTube"
    _platform_url = "https://peertube.tv/w/"

    # optional options available
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
        "align": directives.unchanged,
        "url_parameters": directives.unchanged,
        "server_url": directives.unchanged,
    }


def visit_peertube_node(self, node):
    """Custom html visit node."""
    if "server" in node:
        server = node["server"]
    else:
        server = "peertube.tv"  # default
    node["platform_url"] = f"https://{server}/videos/embed/"
    return utils.visit_video_node_html(self, node)


_NODE_VISITORS = utils._NODE_VISITORS.copy()
_NODE_VISITORS.update(html=(visit_peertube_node, utils.depart_video_node))
