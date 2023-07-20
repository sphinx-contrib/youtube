"""Directive dedicated to the peertube platform."""

from . import utils
from docutils.parsers.rst import directives

# https://docs.joinpeertube.org/api/embed-player

class peertube(utils.video):
    """Empty video node class."""

    pass


class PeerTube(utils.Video):
    """Custom version of the Video Directive."""

    _node = peertube
    _thumbnail_url = ""
    _platform = "PeerTube"

    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
        "align": directives.unchanged,
        "url_parameters": directives.unchanged,
        "server": directives.unchanged,
    }

def visit_peertube_node(self, node):
    """Custom html visit node."""
    server = node["server"]
    if server is None:
        server = "peertube.tv"  # default
    node["platform_url"] = f"https://{server}/videos/embed/"
    return utils.visit_video_node_html(self, node)


_NODE_VISITORS = utils._NODE_VISITORS.copy()
_NODE_VISITORS.update(html=(visit_peertube_node, utils.depart_video_node))
