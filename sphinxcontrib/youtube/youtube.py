"""Directive dedicated to the youtube platform."""

import re

from . import utils

# Matches the video id out of any common form of youtube url:
#   https://www.youtube.com/watch?v=dQw4w9WgXcQ
#   https://youtu.be/dQw4w9WgXcQ
#   https://www.youtube.com/embed/dQw4w9WgXcQ
#   https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ
#   https://www.youtube.com/shorts/dQw4w9WgXcQ
#   https://www.youtube.com/live/dQw4w9WgXcQ
# A bare video id (no match) is left untouched.
_URL_ID_RE = re.compile(
    r"""^(?:(?:https?:)?//)?
        (?:[\w-]+\.)*youtube(?:-nocookie)?\.com/
        (?:watch\?(?:.*&)?v=|embed/|shorts/|live/|v/)
        (?P<id>[\w-]{11})
    |
        ^(?:(?:https?:)?//)?(?:[\w-]+\.)*youtu\.be/(?P<id2>[\w-]{11})
    """,
    re.VERBOSE,
)


class youtube(utils.video):
    """Empty video node class."""

    pass


class YouTube(utils.Video):
    """Custom version of the Video Directive."""

    _node = youtube
    _thumbnail_url = "https://i3.ytimg.com/vi/{}/maxresdefault.jpg"
    _platform = "youtube"
    _platform_url = "https://youtu.be/"

    @classmethod
    def _extract_id(cls, value):
        """Accept either a bare video id or a full youtube url."""
        match = _URL_ID_RE.match(value.strip())
        if match:
            return match.group("id") or match.group("id2")
        return value


def visit_youtube_node(self, node):
    """Custom html visit node."""
    privacy = "https://www.youtube-nocookie.com/embed/"
    embed = "https://www.youtube.com/embed/"
    node["platform_url"] = embed if node["privacy_mode"] is None else privacy
    return utils.visit_video_node_html(
        self,
        node,
        additional_attr={"referrerpolicy": "strict-origin-when-cross-origin"},
    )


_NODE_VISITORS = utils._NODE_VISITORS.copy()
_NODE_VISITORS.update(html=(visit_youtube_node, utils.depart_video_node))
