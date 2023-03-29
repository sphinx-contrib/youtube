"""Directive dedicated to the vimeo platform."""

from . import utils


class vimeo(utils.video):
    """empty video node class."""

    pass


class Vimeo(utils.Video):
    """Custom version of the Video Directive."""

    _node = vimeo
    _thumbnail_url = "https://vumbnail.com/{}.jpg"


def visit_vimeo_node(self, node):
    """Custom html visit node."""
    return utils.visit_video_node(
        self, node, platform_url="https://player.vimeo.com/video/"
    )


def visit_vimeo_node_epub(self, node):
    """Custom epub visit node."""
    return utils.visit_video_node_epub(
        self, node, platform_url="https://player.vimeo.com/video/"
    )


def visit_vimeo_node_latex(self, node):
    """Custom latex visit node."""
    return utils.visit_video_node_latex(
        self, node, platform="vimeo", platform_url="https://player.vimeo.com/video/"
    )


def unsupported_visit_vimeo(self, node):
    """Custom unsuported visit node."""
    return utils.unsupported_visit_video(self, node, platform="vimeo")


_NODE_VISITORS = {
    "html": (visit_vimeo_node, utils.depart_video_node),
    "epub": (visit_vimeo_node_epub, utils.depart_video_node),
    "latex": (visit_vimeo_node_latex, utils.depart_video_node),
    "man": (unsupported_visit_vimeo, None),
    "texinfo": (unsupported_visit_vimeo, None),
    "text": (unsupported_visit_vimeo, None),
}
