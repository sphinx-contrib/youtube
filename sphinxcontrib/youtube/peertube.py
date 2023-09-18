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
    _thumbnail_url = "{}.jpg"
    _platform = "peertube"
    _platform_url = "peertube.tv"

    # optional options available
    option_spec = {
        "width": directives.unchanged,
        "height": directives.unchanged,
        "aspect": directives.unchanged,
        "align": directives.unchanged,
        "url_parameters": directives.unchanged,
        "instance": directives.unchanged,
    }


def visit_peertube_node_html(self, node):
    """Custom html visit node."""
    node["platform_url"] = f"https://{node['instance']}/videos/embed/"
    return utils.visit_video_node_html(self, node)


def visit_video_node_epub(self, node):
    """Custom epub visit node."""
    node["platform_url"] = f"https://{node['instance']}/w/"
    return utils.visit_video_node_epub(self, node)


def visit_video_node_latex(self, node):
    """Custom epub visit node."""
    node["platform_url"] = f"https://{node['instance']}/w/"
    return utils.visit_video_node_latex(self, node)


_NODE_VISITORS = utils._NODE_VISITORS.copy()
_NODE_VISITORS.update(html=(visit_peertube_node_html, utils.depart_video_node))
_NODE_VISITORS.update(epub=(visit_video_node_epub, utils.depart_video_node))
_NODE_VISITORS.update(latex=(visit_video_node_latex, utils.depart_video_node))
