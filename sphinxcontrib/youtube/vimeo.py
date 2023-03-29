"""Directive dedicated to the vimeo platform."""

from . import utils


class vimeo(utils.video):
    """empty video node class."""

    pass


class Vimeo(utils.Video):
    """Custom version of the Video Directive."""

    _node = vimeo
    _thumbnail_url = "https://vumbnail.com/{}.jpg"
    _platform = "vimeo"
    _platform_url = "https://player.vimeo.com/video/"

_NODE_VISITORS = {
    "html": (utils.visit_video_node_html, utils.depart_video_node),
    "epub": (utils.visit_video_node_epub, utils.depart_video_node),
    "latex": (utils.visit_video_node_latex, utils.depart_video_node),
    "man": (utils.visit_video_node_unsupported, utils.depart_video_node),
    "texinfo": (utils.visit_video_node_unsupported, utils.depart_video_node),
    "text": (utils.visit_video_node_unsupported, utils.depart_video_node),
}
