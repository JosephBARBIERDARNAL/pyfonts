from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
from tempfile import NamedTemporaryFile
from matplotlib.font_manager import FontProperties


def _get_font(font_url: str) -> FontProperties:
    with NamedTemporaryFile(delete=False, suffix=".ttf") as temp_file:
        try:
            if not _is_valid_font_url(font_url=font_url):
                raise ValueError(
                    f"""
                    The URL provided ({font_url}) does not appear to be valid.
                    If you think this is an error, please open an issue at 
                    https://github.com/JosephBARBIERDARNAL/pyfonts/issues
                    """
                )
            else:
                response = urlopen(font_url)
                temp_file.write(response.read())
        except HTTPError as e:
            if e.code == 404:
                raise Exception(
                    f"""
                    Font file not found.
                    """
                )
        except URLError:
            raise Exception(
                f"Failed to load font. This may be due to a lack of internet connection"
            )
        font = FontProperties(fname=temp_file.name)
    return font


def _add_font_locally(font_url: str, destination_path: str, verbose: bool) -> None:
    if not destination_path.endswith(".ttf"):
        destination_path += ".ttf"
    try:
        if not _is_valid_font_url(font_url=font_url):
            raise ValueError(
                f"""
                The URL provided ({font_url}) does not appear to be valid.
                If you think this is an error, please open a folder at the following address
                https://github.com/JosephBARBIERDARNAL/pyfonts/issues
                """
            )
        else:
            response = urlopen(font_url)
            with open(destination_path, "wb") as out_file:
                out_file.write(response.read())
                if verbose:
                    print(f"Font installed at: {destination_path}")
    except HTTPError as e:
        if e.code == 404:
            raise ValueError(f"No font file found at {font_url}")


def _is_valid_font_url(font_url: str) -> bool:

    try:
        result = urlparse(font_url)
        if not all([result.scheme, result.netloc, result.path]):
            return False
    except:
        return False
    
    if result.scheme not in ['http', 'https']:
        return False
    
    return True