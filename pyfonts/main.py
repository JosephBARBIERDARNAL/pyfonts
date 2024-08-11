from matplotlib.font_manager import FontProperties
import os

from .utils import _get_font, _add_font_locally


def load_font(font_location: str) -> FontProperties:
    """
    Loads a font from the exact URL provided.

    Parameters:
    - font_location (str): The exact URL of a font file.

    Returns:
    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.
    """
    font = _get_font(font_location=font_location)
    return font


def download_font(
    font_location: str,
    destination_path: str | None = None,
    verbose=True,
) -> None:
    """
    Download a font from the exact URL provided.

    Parameters:
    - font_location (str): The exact URL of a font file.
    - destination_path (str): The path where the font file will be saved. If None, it will be saved in the current working directory.

    Returns:
    - None
    """
    if destination_path is None:
        destination_path = os.path.join(os.getcwd(), f"{font_location.split('/')[-1]}")
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    _add_font_locally(
        font_location=font_location, destination_path=destination_path, verbose=verbose
    )
