import pytest
from pyfonts.is_valid import _is_valid_raw_url, _is_url, _is_safe_input


def test_safe_input():
    assert _is_safe_input("font_name", None, None) == True
    assert _is_safe_input(None, "font_url", None) == True
    assert _is_safe_input(None, None, "font_path") == True
    assert _is_safe_input("font_name", "font_url", None) == False
    assert _is_safe_input(None, "font_url", "font_path") == False
    assert _is_safe_input("font_name", None, "font_path") == False
    assert _is_safe_input("font_name", "font_url", "font_path") == False
    assert _is_safe_input(None, None, None) == False
    assert _is_safe_input("font_name", "font_url", "font_path") == False


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("https://www.example.com", True),
        ("http://example.com", True),
        ("ftp://ftp.example.com", True),
        ("www.example.com", False),
        ("example.com", False),
        ("just a string", False),
        ("", False),
        ("file:///C:/Users/username/Documents/file.txt", True),
        ("mailto:user@example.com", True),
    ],
)
def test_is_url(input_string, expected_result):
    assert _is_url(input_string) == expected_result


def test_is_url_type_error():
    with pytest.raises(AttributeError):
        _is_url(123)


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://github.com/user/repo/blob/master/font.ttf?raw=true", True),
        ("https://github.com/user/repo/raw/master/font.otf", True),
        ("https://raw.githubusercontent.com/user/repo/master/font.woff", True),
        (
            "https://raw.githubusercontent.com/user/repo/branch-name/subfolder/font.woff2",
            True,
        ),
        ("https://github.com/user/repo/blob/master/font.ttf", False),
        ("https://github.com/user/repo/raw/master/font.txt", False),
        ("https://raw.githubusercontent.com/user/repo/master/font.exe", False),
        ("https://example.com/font.ttf", False),
        ("https://github.com/user/repo/tree/master/fonts/font.ttf", False),
        ("https://github.com/user/repo/blob/master/font.ttf?raw=false", False),
        (
            "https://github.com/user/repo/blob/master/font.ttf?raw=true&param=value",
            False,
        ),
        ("https://github.com/user/repo/raw/master/font.WOFF", False),
        ("https://raw.githubusercontent.com/user/repo/master/font.ttf?raw=true", False),
    ],
)
def test_is_valid_raw_url(url, expected):
    assert _is_valid_raw_url(url) == expected


def test_is_valid_raw_url_with_empty_string():
    assert _is_valid_raw_url("") == False


def test_is_valid_raw_url_with_none():
    with pytest.raises(TypeError):
        _is_valid_raw_url(None)


def test_is_valid_raw_url_with_non_string():
    with pytest.raises(TypeError):
        _is_valid_raw_url(123)
