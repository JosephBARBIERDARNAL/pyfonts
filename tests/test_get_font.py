import pytest
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError, URLError
from matplotlib.font_manager import FontProperties
from pyfonts.main import _get_font


@pytest.fixture
def mock_urlopen():
    with patch("pyfonts.utils.urlopen") as mock:
        yield mock


@pytest.fixture
def mock_is_valid_font_url():
    with patch("pyfonts.utils._is_valid_font_url") as mock:
        yield mock


def test_get_font_success(mock_urlopen, mock_is_valid_font_url):
    mock_is_valid_font_url.return_value = True
    mock_response = MagicMock()
    mock_response.read.return_value = b"mock font data"
    mock_urlopen.return_value = mock_response

    result = _get_font("http://example.com/font.ttf")

    assert isinstance(result, FontProperties)


def test_get_font_invalid_url(mock_is_valid_font_url):
    mock_is_valid_font_url.return_value = False

    with pytest.raises(
        ValueError, match="The URL provided .* does not appear to be valid"
    ):
        _get_font("invalid_url")


def test_get_font_http_error(mock_urlopen, mock_is_valid_font_url):
    mock_is_valid_font_url.return_value = True
    mock_urlopen.side_effect = HTTPError(
        "http://example.com", 404, "Not Found", {}, None
    )

    with pytest.raises(Exception, match="Font file not found"):
        _get_font("http://example.com/font.ttf")


def test_get_font_url_error(mock_urlopen, mock_is_valid_font_url):
    mock_is_valid_font_url.return_value = True
    mock_urlopen.side_effect = URLError("No internet connection")

    with pytest.raises(Exception, match="Failed to load font"):
        _get_font("http://example.com/font.ttf")
