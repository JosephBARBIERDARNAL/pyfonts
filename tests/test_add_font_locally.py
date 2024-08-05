import pytest
from unittest.mock import patch, mock_open
from urllib.error import HTTPError
from pyfonts.main import _add_font_locally


@pytest.fixture
def mock_urlopen():
    with patch("pyfonts.utils.urlopen") as mock:
        yield mock


@pytest.fixture
def mock_is_valid_font_url():
    with patch("pyfonts.utils._is_valid_font_url") as mock:
        yield mock


def test_add_font_locally_success(mock_urlopen, mock_is_valid_font_url, capsys):
    mock_is_valid_font_url.return_value = True
    mock_response = mock_urlopen.return_value
    mock_response.read.return_value = b"mock font data"

    m = mock_open()
    with patch("builtins.open", m):
        _add_font_locally("http://example.com/font.ttf", "/path/to/font.ttf", True)

    m.assert_called_once_with("/path/to/font.ttf", "wb")
    m().write.assert_called_once_with(b"mock font data")
    captured = capsys.readouterr()
    assert "Font installed at: /path/to/font.ttf" in captured.out


def test_add_font_locally_invalid_url(mock_is_valid_font_url):
    mock_is_valid_font_url.return_value = False

    with pytest.raises(
        ValueError, match="The URL provided .* does not appear to be valid"
    ):
        _add_font_locally("invalid_url", "/path/to/font.ttf", True)


def test_add_font_locally_http_error(mock_urlopen, mock_is_valid_font_url):
    mock_is_valid_font_url.return_value = True
    mock_urlopen.side_effect = HTTPError(
        "http://example.com", 404, "Not Found", {}, None
    )

    with pytest.raises(
        ValueError, match="No font file found at http://example.com/font.ttf"
    ):
        _add_font_locally("http://example.com/font.ttf", "/path/to/font.ttf", True)
