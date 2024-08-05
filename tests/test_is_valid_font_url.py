import pytest
from pyfonts.utils import _is_valid_font_url


@pytest.mark.parametrize(
    "url,expected",
    [
        ("http://example.com/font.ttf", True),
        ("https://example.com/font.ttf", True),
        ("ftp://example.com/font.ttf", False),
        ("http://", False),
        ("example.com", False),
        ("", False),
        (
            "http://example.com",
            False,
        ),  # This is technically a valid URL, though it might not point to a font file
        ("https://example.com/path/to/font.ttf", True),
    ],
)
def test_is_valid_font_url(url, expected):
    assert _is_valid_font_url(url) == expected


def test_is_valid_font_url_exception():
    assert _is_valid_font_url(None) == False
