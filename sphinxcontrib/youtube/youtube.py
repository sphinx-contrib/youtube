#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import utils
from functools import partial


class youtube(utils.video):
    pass


class YouTube(utils.Video):
    _node = youtube


visit_youtube_node = partial(utils.visit_video_node,
                             platform_url="https://www.youtube.com/embed/")


visit_youtube_node_latex = partial(utils.visit_video_node_latex,
                                   platform="youtube",
                                   platform_url="https://youtu.be/")


unsupported_visit_youtube = partial(utils.unsupported_visit_video,
                                    platform="youtube")


_NODE_VISITORS = {
    'html': (visit_youtube_node, utils.depart_video_node),
    'latex': (visit_youtube_node_latex, utils.depart_video_node),
    'man': (unsupported_visit_youtube, None),
    'texinfo': (unsupported_visit_youtube, None),
    'text': (unsupported_visit_youtube, None)
}
