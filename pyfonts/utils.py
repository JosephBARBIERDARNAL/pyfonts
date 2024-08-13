from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
from tempfile import NamedTemporaryFile
from matplotlib.font_manager import FontProperties
from pyfonts.is_url import _is_url, _is_valid_raw_url


def _get_font(font_location: str) -> FontProperties:
    """ """

    is_an_url = _is_url(font_location)

    if not is_an_url:
        font = FontProperties(fname=font_location)
        try:
            font.get_name()
        except FileNotFoundError:
            raise ValueError(f"Font file not found at : '{font_location}'")
        return font

    else:
        with NamedTemporaryFile() as temp_file:
            try:
                if not _is_valid_raw_url(font_location=font_location):
                    raise ValueError(
                        f"""
                        The URL provided ({font_location}) does not appear to be valid.
                        If you pass an url to PyFonts, it must point to a binary font file from Github.
                        Learn more at: https://github.com/JosephBARBIERDARNAL/pyfonts?tab=readme-ov-file#how-to-find-fonts
                        """
                    )
                else:
                    response = urlopen(font_location)
                    temp_file.write(response.read())
            except HTTPError as e:
                if e.code == 404:
                    raise Exception(
                        """
                        404 error. The url passed does not point to a valid url: font file not found.
                        """
                    )
            except URLError:
                raise Exception(
                    "Failed to load font. This may be due to a lack of internet connection."
                )
            font = FontProperties(fname=temp_file.name)
            return font


def _add_font_locally(font_location: str, destination_path: str, verbose: bool) -> None:
    if not destination_path.endswith(".ttf"):
        destination_path += ".ttf"
    try:
        if not _is_valid_font_url(font_location=font_location):
            raise ValueError(
                f"""
                The URL provided ({font_location}) does not appear to be valid.
                If you think this is an error, please open a folder at the following address
                https://github.com/JosephBARBIERDARNAL/pyfonts/issues
                """
            )
        else:
            response = urlopen(font_location)
            with open(destination_path, "wb") as out_file:
                out_file.write(response.read())
                if verbose:
                    print(f"Font installed at: {destination_path}")
    except HTTPError as e:
        if e.code == 404:
            raise ValueError(f"No font file found at {font_location}")


def _is_valid_font_url(font_location: str) -> bool:
    try:
        result = urlparse(font_location)
        if not all([result.scheme, result.netloc, result.path]):
            return False
    except Exception as e:
        print(e)
        return False

    if result.scheme not in ["http", "https"]:
        return False

    return True
