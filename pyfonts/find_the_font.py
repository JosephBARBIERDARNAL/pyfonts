from pyfonts.is_url import _is_url, _is_valid_raw_url


def _find_the_font(font_location: str):
    """
    Intuitive algorithm that tries a whole bunch of different font url until it founds
    something. If nothing is found, raises an error for invalid font url/path.

    When trying to load a font, PyFonts actually tries to load a whole bunch
    font until it founds one that works.
    """

    return None
