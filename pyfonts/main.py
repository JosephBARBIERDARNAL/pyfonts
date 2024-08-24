from matplotlib.font_manager import FontProperties
from typing import Optional

from .get_font import _get_font_from_url, _get_local_font, _get_font_from_google
from .is_valid import _is_safe_input


def load_font(
    font_url: Optional[str] = None,
    font_path: Optional[str] = None,
    font_name: Optional[str] = None,
    weight: Optional[str] = None,
    style: Optional[str] = None,
) -> FontProperties:
    """
    Loads a font from one of the following:
        - An url that points to a binary font file if `font_url`
        - A locally stored font if `font_path`
        - A font from Google font repo if `font_name`

    Parameters:
    - font_url (Optional[str]): A URL pointing to a binary font file.
    - font_path (Optional[str]): The local file path of the font.
    - font_name (Optional[str]): The name of the font to load from Google Fonts.
    - weight (Optional[str]): The weight of the font to load.
    - style (Optional[str]):

    Returns:
    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.
    """

    if not _is_safe_input(font_name, font_url, font_path):
        raise ValueError(
            "You must provide only one of the following: `font_name`, `font_url` or `font_path`."
        )

    if font_url:
        font = _get_font_from_url(font_url)

    elif font_path:
        font = _get_local_font(font_path)

    elif font_name:
        font = _get_font_from_google(font_name, weight=weight, style=style)

    return font
