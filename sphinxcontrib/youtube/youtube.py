"""Directive dedicated to the youtube platform."""

from . import utils


class youtube(utils.video):
    """empty video node class."""

    pass


class YouTube(utils.Video):
    """Custom version of the Video Directive."""

    _node = youtube
    _thumbnail_url = "https://i3.ytimg.com/vi/{}/maxresdefault.jpg"
    _platform = "youtube"
    _platform_url="https://youtu.be/"
    _platform_url_privacy="https://www.youtube-nocookie.com/embed/"


def visit_youtube_node(self, node):
    """Custom html visit node."""
    node["platform_url"] = "https://www.youtube.com/embed/"
    return utils.visit_video_node_html(self,node)


_NODE_VISITORS = {
    "html": (visit_youtube_node, utils.depart_video_node),
    "epub": (utils.visit_video_node_epub, utils.depart_video_node),
    "latex": (utils.visit_video_node_latex, utils.depart_video_node),
    "man": (utils.visit_video_node_unsupported, utils.depart_video_node),
    "texinfo": (utils.visit_video_node_unsupported, utils.depart_video_node),
    "text": (utils.visit_video_node_unsupported, utils.depart_video_node),
}
