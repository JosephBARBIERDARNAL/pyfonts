from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from tempfile import NamedTemporaryFile
from matplotlib.font_manager import FontProperties


def _get_font(font_url: str):
    with NamedTemporaryFile(delete=False, suffix=".ttf") as temp_file:
        try:
            response = urlopen(font_url)
            temp_file.write(response.read())
        except HTTPError as e:
            if e.code == 404:
                url_to_check = font_url.rsplit("/", 1)[0]
                url_to_check = "https://github.com/google/fonts/"
                raise Exception(
                    f"Font file not found.\nPlease check if your font is available at: {url_to_check}"
                )
            else:
                raise Exception(f"HTTP Error {e.code}: {e.reason}")
        except URLError:
            raise Exception(
                f"Failed to load font. This may be due to a lack of internet connection"
            )
        font = FontProperties(fname=temp_file.name)
    return font


def _add_font_locally(font_url: str, destination_path: str, verbose: bool) -> None:
    try:
        response = urlopen(font_url)
        with open(destination_path, "wb") as out_file:
            out_file.write(response.read())
            if verbose:
                print(f"Font installed at: {destination_path}")
    except HTTPError as e:
        if e.code == 404:
            raise ValueError(f"No font file found at {font_url}")


def _get_font_url(
    family: str,
    mapped_style: str = "Regular",
    license: str = "ofl",
):
    AVAILABLE_STYLE = [
        "Regular",
        "Bold",
        "Italic",
        "BoldItalic",
        "ExtraBold",
        "ExtraBoldItalic",
        "ExtraLight",
        "ExtraLightItalic",
        "Light",
        "LightItalic",
        "Medium",
        "MediumItalic",
        "SemiBold",
        "SemiBoldItalic",
        "Thin",
        "ThinItalic",
    ]

    if mapped_style not in AVAILABLE_STYLE:
        raise ValueError(
            f"`mapped_style` ({mapped_style}) must be in {AVAILABLE_STYLE}"
        )

    google_repo_with_fonts = f"https://github.com/google/fonts/raw/main/{license}"
    ttf_name = family + "-" + mapped_style + ".ttf"
    folder_with_fonts = f"{google_repo_with_fonts}/{family.lower()}"
    font_url = f"{folder_with_fonts}/{ttf_name}"
    return font_url


def _map_weight_and_style(weight: str, style: str) -> str:
    weight = weight.lower()
    style = style.lower()

    if weight not in [
        "normal",
        "bold",
        "light",
        "medium",
        "semibold",
        "extrabold",
        "thin",
    ]:
        raise ValueError(
            "Invalid weight. Must be 'normal', 'bold', 'light', 'medium', 'semibold', 'extrabold', or 'thin'."
        )

    if style not in ["normal", "italic"]:
        raise ValueError("Invalid style. Must be 'normal' or 'italic'.")

    if weight == "normal" and style == "normal":
        return "Regular"
    elif weight == "normal" and style == "italic":
        return "Italic"
    elif weight == "bold" and style == "normal":
        return "Bold"
    elif weight == "bold" and style == "italic":
        return "BoldItalic"
    elif weight == "light" and style == "normal":
        return "Light"
    elif weight == "light" and style == "italic":
        return "LightItalic"
    elif weight == "medium" and style == "normal":
        return "Medium"
    elif weight == "medium" and style == "italic":
        return "MediumItalic"
    elif weight == "semibold" and style == "normal":
        return "SemiBold"
    elif weight == "semibold" and style == "italic":
        return "SemiBoldItalic"
    elif weight == "extrabold" and style == "normal":
        return "ExtraBold"
    elif weight == "extrabold" and style == "italic":
        return "ExtraBoldItalic"
    elif weight == "thin" and style == "normal":
        return "Thin"
    elif weight == "thin" and style == "italic":
        return "ThinItalic"
