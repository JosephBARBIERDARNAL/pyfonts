import pytest
from unittest.mock import patch
from matplotlib.font_manager import FontProperties
from pyfonts import load_font


@pytest.fixture
def mock_get_font():
    with patch("pyfonts.main._get_font") as mock:
        yield mock


def test_load_font_success(mock_get_font):
    mock_font = FontProperties()
    mock_get_font.return_value = mock_font

    result = load_font("http://example.com/font.ttf")

    assert isinstance(result, FontProperties)
    mock_get_font.assert_called_once_with(font_location="http://example.com/font.ttf")


def test_load_font_failure(mock_get_font):
    mock_get_font.side_effect = Exception("Font loading failed")

    with pytest.raises(Exception, match="Font loading failed"):
        load_font("http://example.com/invalid_font.ttf")
