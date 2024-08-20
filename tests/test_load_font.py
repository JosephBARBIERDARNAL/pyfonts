import pytest
from unittest.mock import patch
from matplotlib.font_manager import FontProperties
from pyfonts import load_font


@pytest.fixture(autouse=True)
def mock_imported_functions():
    with patch("pyfonts.is_valid._is_safe_input") as mock_is_safe_input, patch(
        "pyfonts.get_font._get_font_from_url"
    ) as mock_get_font_from_url, patch(
        "pyfonts.get_font._get_local_font"
    ) as mock_get_local_font, patch(
        "pyfonts.get_font._get_font_from_google"
    ) as mock_get_font_from_google:
        mock_is_safe_input.return_value = True
        mock_get_font_from_url.return_value = FontProperties()
        mock_get_local_font.return_value = FontProperties()
        mock_get_font_from_google.return_value = FontProperties()

        yield (
            mock_is_safe_input,
            mock_get_font_from_url,
            mock_get_local_font,
            mock_get_font_from_google,
        )


def test_load_font_with_url():
    font = load_font(
        font_url="https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
    )
    assert isinstance(font, FontProperties)


def test_load_font_with_path():
    font = load_font(font_path="tests/Ultra-Regular.ttf")
    assert isinstance(font, FontProperties)


def test_load_font_invalid_input():
    with pytest.raises(ValueError):
        load_font(font_url="http://example.com/font.ttf", font_path="/path/to/font.ttf")


def test_load_font_no_input():
    with pytest.raises(ValueError):
        load_font()


def test_load_font_unsafe_input(mock_imported_functions):
    mock_is_safe_input, _, _, _ = mock_imported_functions
    mock_is_safe_input.return_value = False

    with pytest.raises(ValueError):
        load_font(font_url="http://example.com/font.ttf")
