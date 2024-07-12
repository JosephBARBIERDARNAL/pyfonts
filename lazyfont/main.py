from matplotlib.font_manager import FontProperties
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from tempfile import NamedTemporaryFile
import warnings
import os

from .utils import _get_font_url, _map_weight_and_style, _get_font, _add_font_locally


def load_font(
    family: str,
    weight: str = "normal",
    style: str = "normal",
    license: str = "ofl",
) -> FontProperties:
    """
    Loads a font from the Google Fonts repository.

    Parameters:
    - family (str): The name of the font family to load.
    - weight (str): The weight of the font to load (default is 'normal'). Must be one of:
       'normal', 'bold', 'light', 'medium', 'semibold', 'extrabold', 'thin'
    - style (str): The style of the font to load (default is 'normal'). Must be one of:
       'normal', 'italic'
    - license (str): directory name of the Google font Github repository. Default to `ofl` (Open Font License)

    Returns:
    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.
    """
    mapped_style = _map_weight_and_style(weight, style)
    font_url = _get_font_url(family=family, mapped_style=mapped_style, license=license)
    font = _get_font(font_url)
    return font


def load_exact_font(font_url: str) -> FontProperties:
    """
    Loads a font from the exact URL provided.

    Parameters:
    - font_url (str): The exact URL of a font file.

    Returns:
    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.
    """
    font = _get_font(font_url=font_url)
    return font


def download_font(
    family: str,
    weight: str = "normal",
    style: str = "normal",
    license: str = "ofl",
    destination_path: str = None,
    verbose=True,
) -> None:
    """
    Download locally a font from the Google Fonts repository.

    Parameters:
    - family (str): The name of the font family to load.
    - weight (str): The weight of the font to load (default is 'normal'). Must be one of:
       'normal', 'bold', 'light', 'medium', 'semibold', 'extrabold', 'thin'
    - style (str): The style of the font to load (default is 'normal'). Must be one of:
       'normal', 'italic'
    - license (str): directory name of the Google font Github repository. Default to `ofl` (Open Font License)
    - destination_path (str): The path where the font file will be saved. If None, it will be saved in the current working directory.

    Returns:
    - None
    """
    mapped_style = _map_weight_and_style(weight, style)
    if destination_path is None:
        destination_path = os.path.join(os.getcwd(), f"{family}_{mapped_style}.ttf")

    font_url = _get_font_url(family=family, mapped_style=mapped_style, license=license)
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    _add_font_locally(
        font_url=font_url, destination_path=destination_path, verbose=verbose
    )


def download_exact_font(
    font_url: str,
    destination_path: str = None,
    verbose=True,
) -> None:
    """
    Download a font from the exact URL provided.

    Parameters:
    - font_url (str): The exact URL of a font file.
    - destination_path (str): The path where the font file will be saved. If None, it will be saved in the current working directory.

    Returns:
    - None
    """
    if destination_path is None:
        destination_path = os.path.join(
            os.getcwd(), f"{font_url.split('/')[-1]}"
        )
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    _add_font_locally(
        font_url=font_url, destination_path=destination_path, verbose=verbose
    )
