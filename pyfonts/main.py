from matplotlib.font_manager import FontProperties
from typing import Optional

from .get_font import _get_font_from_url, _get_local_font


def load_font(
    font_url: Optional[str] = None,
    font_path: Optional[str] = None,
) -> FontProperties:
    """
    Loads a font from one of the following:
        - An url that points to a binary font file if `font_url`
        - A locally stored font if `font_path`

    Parameters:
    - font_url (Optional[str]): A URL pointing to a binary font file from Github.
    - font_path (Optional[str]): The local file path of the font.

    Returns:
    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.
    """
    if font_url and font_path:
        raise ValueError(
            "You must provide only one of the following: `font_url` or `font_path`."
        )
    elif font_url:
        font = _get_font_from_url(font_url)
    elif font_path:
        font = _get_local_font(font_path)
    else:
        raise ValueError(
            "You must provide one of the following: `font_url` or `font_path`."
        )
    return font
