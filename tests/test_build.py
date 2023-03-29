"""Test sphinxcontrib.video extension."""

import pytest
from bs4 import BeautifulSoup, formatter

fmt = formatter.HTMLFormatter(indent=2, void_element_close_prefix=" /")


# -- HTML related tests --------------------------------------------------------

@pytest.mark.sphinx(testroot="video")
def test_youtube_html(app, status, warning, file_regression):
    """Test a youtube video in html build."""
    app.builder.build_all()

    html = (app.outdir / "youtube.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")
    video = html.select(".video_wrapper")[0].prettify(formatter=fmt)
    file_regression.check(video, basename="youtube", extension=".html")

@pytest.mark.sphinx(testroot="video")
def test_vimeo_html(app, status, warning, file_regression):
    """Test a youtube video in html build."""
    app.builder.build_all()

    html = (app.outdir / "vimeo.html").read_text(encoding="utf8")
    html = BeautifulSoup(html, "html.parser")
    video = html.select(".video_wrapper")[0].prettify(formatter=fmt)
    file_regression.check(video, basename="vimeo", extension=".html")

# -- Latex related tests -------------------------------------------------------

@pytest.mark.sphinx("latex", testroot="video")
def test_latex(app, status, warning):
    """Test a youtube video in latex build."""
    app.builder.build_all()
    result = (app.outdir / "test-video.tex").read_text(encoding="utf8")

    assert r"\newcommand{\sphinxcontribyoutube}" in result
    assert r"\newcommand{\sphinxcontribvimeo}" in result

    assert r"\sphinxcontribyoutube{https://youtu.be/}{dQw4w9WgXcQ}{}" in result
    assert r"\sphinxcontribvimeo{https://player.vimeo.com/video/}{148751763}{}" in result

# -- Epub related tests --------------------------------------------------------

@pytest.mark.sphinx("epub", testroot="video")
def test_youtube_epub(app, status, warning, file_regression):
    """Test a youtube video in epub build."""
    app.builder.build_all()

    xhtml = (app.outdir / "youtube.xhtml").read_text(encoding="utf8")
    xhtml = BeautifulSoup(xhtml, "html.parser")
    video = xhtml.select(".video_link_url")[0].prettify(formatter=fmt)
    file_regression.check(video, basename="youtube", extension=".xhtml")

@pytest.mark.sphinx("epub", testroot="video")
def test_vimeo_epub(app, status, warning, file_regression):
    """Test a youtube video in epub build."""
    app.builder.build_all()

    xhtml = (app.outdir / "vimeo.xhtml").read_text(encoding="utf8")
    xhtml = BeautifulSoup(xhtml, "html.parser")
    video = xhtml.select(".video_link_url")[0].prettify(formatter=fmt)
    file_regression.check(video, basename="vimeo", extension=".xhtml")

# -- Unsuported builders -------------------------------------------------------

@pytest.mark.sphinx("text", testroot="video")
def test_youtube_unsupported(app, status, warning):
    """Test a youtube video in unsuprted build."""
    app.builder.build_all()

    assert "unsupported output format (node skipped)" in warning.getvalue()