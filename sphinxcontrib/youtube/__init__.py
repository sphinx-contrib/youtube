"""Sphinx "youtube" extension."""
from . import utils, vimeo, youtube, peertube

__version__ = "1.3.0"


def setup(app):
    """Setup Sphinx application."""
    app.add_node(youtube.youtube, **youtube._NODE_VISITORS)
    app.add_directive("youtube", youtube.YouTube)
    app.add_node(vimeo.vimeo, **utils._NODE_VISITORS)
    app.add_directive("vimeo", vimeo.Vimeo)
    app.add_node(peertube.peertube, **peertube._NODE_VISITORS)
    app.add_directive("vimeo", peertube.PeerTube)
    app.connect("builder-inited", utils.configure_image_download)
    app.connect("env-merge-info", utils.merge_download_images)
    app.connect("env-updated", utils.download_images)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
