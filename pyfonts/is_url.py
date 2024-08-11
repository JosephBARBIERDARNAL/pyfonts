import re
from urllib.parse import urlparse


def _is_url(s: str) -> bool:
    """
    Tests whether a string is an url.

    Parameters:
       - s: a string.

    Returns:
       - a boolean indicating whether the string is an url or not.
    """
    is_an_url = urlparse(s).scheme != ""
    return is_an_url


def _is_valid_raw_url(url: str) -> bool:
    """
    Tests whether an url from Github pointing to a font
    is actually a raw url (e.g pointing to the binary font file and not the Github view).

    There are 3 ways/patterns to point to the raw version of a file from Github that are defined
    in `patterns`.

    Parameters:
       - url: the url of the font file.

    Returns:
       - a boolean indicating whether the url corresponds to a raw file.
    """
    patterns = [
        r"^https://github\.com/[^/]+/[^/]+/blob/[^/]+/.+\.(ttf|otf|woff|woff2)\?raw=true$",
        r"^https://github\.com/[^/]+/[^/]+/raw/[^/]+/.+\.(ttf|otf|woff|woff2)$",
        r"^https://raw\.githubusercontent\.com/[^/]+/[^/]+/[^/]+/.+\.(ttf|otf|woff|woff2)$",
    ]

    for pattern in patterns:
        if re.match(pattern, url):
            return True

    return False
