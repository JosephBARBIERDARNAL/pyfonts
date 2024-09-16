import pytest
from unittest.mock import patch
from matplotlib.font_manager import FontProperties
from pyfonts import load_font


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
