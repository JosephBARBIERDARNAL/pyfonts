from matplotlib.font_manager import FontProperties
from typing import Optional

from .get_font import _get_font_from_url, _get_local_font, _get_font_from_google


def load_font(
    font_name: Optional[str] = None,
    font_url: Optional[str] = None,
    font_path: Optional[str] = None,
    weight: Optional[str] = None,
    style: Optional[str] = None,
) -> FontProperties:
    """
    Loads a font from one of the following:
        - Google font repo if `font_name`
        - An url that points to a binary font file if `font_url`
        - A locally stored font if `font_path`

    Parameters:
    - font_name (Optional[str]): The name of the font to load from Google Fonts.
    - font_url (Optional[str]): A URL pointing to a binary font file.
    - font_path (Optional[str]): The local file path of the font.
    - weight (Optional[str]): TODO
    - style (Optional[str]): TODO

    Returns:
    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.
    """

    if font_url:
        font = _get_font_from_url(font_url)

    elif font_path:
        font = _get_local_font(font_path)

    elif font_name:
        font = _get_font_from_google(font_name, weight=weight, style=style)

    return font
