import pytest
from unittest.mock import patch, MagicMock
from matplotlib.font_manager import FontProperties
from pyfonts import preview_font, load_font


@pytest.fixture
def mock_load_font():
    with patch("pyfonts.load_font") as mock:
        mock.return_value = FontProperties()
        yield mock


def test_preview_font_raises_value_error_on_invalid_input(mock_load_font):
    mock_load_font.side_effect = ValueError(
        "You must provide only one of the following: `font_name`, `font_url` or `font_path`."
    )
    with pytest.raises(ValueError):
        preview_font(
            font_url="http://example.com/font.ttf", font_path="/path/to/font.ttf"
        )
