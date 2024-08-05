import pytest
import os
from unittest.mock import patch
from pyfonts import download_font


@pytest.fixture
def mock_add_font_locally():
    with patch("pyfonts.main._add_font_locally") as mock:
        yield mock


def test_download_font_with_destination(mock_add_font_locally, tmp_path):
    destination = tmp_path / "fonts" / "new_font.ttf"
    download_font("http://example.com/font.ttf", str(destination))

    mock_add_font_locally.assert_called_once_with(
        font_url="http://example.com/font.ttf",
        destination_path=str(destination),
        verbose=True,
    )


def test_download_font_without_destination(mock_add_font_locally):
    with patch("os.getcwd", return_value="/home/user"):
        with patch("os.makedirs") as mock_makedirs:
            download_font("http://example.com/font.ttf")

            expected_path = "/home/user/font.ttf"
            mock_add_font_locally.assert_called_once_with(
                font_url="http://example.com/font.ttf",
                destination_path=expected_path,
                verbose=True,
            )
            mock_makedirs.assert_called_once_with("/home/user", exist_ok=True)


def test_download_font_verbose_false(mock_add_font_locally):
    download_font("http://example.com/font.ttf", verbose=False)

    mock_add_font_locally.assert_called_once_with(
        font_url="http://example.com/font.ttf",
        destination_path=os.path.join(os.getcwd(), "font.ttf"),
        verbose=False,
    )
