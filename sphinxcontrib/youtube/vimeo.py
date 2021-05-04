#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import utils
from functools import partial


class vimeo(utils.video):
    pass


class Vimeo(utils.Video):
    _node = vimeo


visit_vimeo_node = partial(utils.visit_video_node,
                           platform_url="https://player.vimeo.com/video/")


visit_vimeo_node_latex = partial(utils.visit_video_node_latex,
                                 platform="vimeo",
                                 platform_url="https://player.vimeo.com/video/")


unsupported_visit_vimeo = partial(utils.unsupported_visit_video,
                                  platform="vimeo")


_NODE_VISITORS = {
    'html': (visit_vimeo_node, utils.depart_video_node),
    'latex': (visit_vimeo_node_latex, utils.depart_video_node),
    'man': (unsupported_visit_vimeo, None),
    'texinfo': (unsupported_visit_vimeo, None),
    'text': (unsupported_visit_vimeo, None)
}
