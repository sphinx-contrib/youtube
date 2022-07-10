"""Some basic tests for the extension."""


def test_yt_posttransform_html(sphinx_doctree):
    """Test AST output, after post-transforms, when using the HTML builder."""
    sphinx_doctree.set_conf({"extensions": ["sphinxcontrib.youtube"]})
    sphinx_doctree.buildername = "html"
    result = sphinx_doctree("""\

.. youtube:: dQw4w9WgXcQ

""")
    assert not result.warnings
    assert result.get_resolved_pformat().strip() == (
        '<document source="<src>/index.rst">\n'
        '    <youtube align="True" aspect="True" height="True" '
        'id="dQw4w9WgXcQ" privacy_mode="True" url_parameters="" width="True">'
    )


def test_vim_posttransform_html(sphinx_doctree):
    """Test AST output, after post-transforms, when using the HTML builder."""
    sphinx_doctree.set_conf({"extensions": ["sphinxcontrib.youtube"]})
    sphinx_doctree.buildername = "html"
    result = sphinx_doctree(
        """\

.. vimeo:: 148751763

"""
    )
    assert not result.warnings
    assert result.get_resolved_pformat().strip() == (
        '<document source="<src>/index.rst">\n'
        '    <vimeo align="True" aspect="True" height="True" '
        'id="148751763" privacy_mode="True" url_parameters="" width="True">'
    )
