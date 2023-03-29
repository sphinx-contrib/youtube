"""Directive dedicated to the youtube platform."""

from . import utils


class youtube(utils.video):
    """empty video node class."""

    pass


class YouTube(utils.Video):
    """Custom version of the Video Directive."""

    _node = youtube
    _thumbnail_url = "https://i3.ytimg.com/vi/{}/maxresdefault.jpg"


def visit_youtube_node(self, node):
    """Custom html visit node."""
    return utils.visit_video_node(
        self,
        node,
        platform_url="https://www.youtube.com/embed/",
        platform_url_privacy="https://www.youtube-nocookie.com/embed/",
    )


def visit_youtube_node_epub(self, node):
    """Custom epub visit node."""
    return utils.visit_video_node_epub(self, node, platform_url="https://youtu.be/")


def visit_youtube_node_latex(self, node):
    """Custom latex visit node."""
    return utils.visit_video_node_latex(
        self, node, platform="youtube", platform_url="https://youtu.be/"
    )


def unsupported_visit_youtube(self, node):
    """Custom unsupported visit node."""
    return utils.unsupported_visit_video(self, node, platform="youtube")


_NODE_VISITORS = {
    "html": (visit_youtube_node, utils.depart_video_node),
    "epub": (visit_youtube_node_epub, utils.depart_video_node),
    "latex": (visit_youtube_node_latex, utils.depart_video_node),
    "man": (unsupported_visit_youtube, None),
    "texinfo": (unsupported_visit_youtube, None),
    "text": (unsupported_visit_youtube, None),
}
