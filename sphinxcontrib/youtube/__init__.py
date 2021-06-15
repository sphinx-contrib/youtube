from  . import youtube, vimeo

def setup(app):
    app.add_node(youtube.youtube, **youtube._NODE_VISITORS)
    app.add_directive("youtube", youtube.YouTube)
    app.add_node(vimeo.vimeo, **vimeo._NODE_VISITORS)
    app.add_directive("vimeo", vimeo.Vimeo)
