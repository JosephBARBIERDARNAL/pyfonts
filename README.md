# PyFonts

<img src="logo.png" alt="pyfonts logo" align="right" width="200px"/>

A simple way to load fonts for matplotlib.

<br>

Check out the [online documentation](https://pyfonts.streamlit.app/).

Table of content:

- [Quick Start](#quick-start)
- [Find fonts](#how-to-find-fonts)
- [Fonts in Matplotlib](#pyfonts-and-matplotlib)
- [Other feature: download fonts](#other-feature-download-a-font-locally)

<br><br>

# Installation

```
pip install git+https://github.com/JosephBARBIERDARNAL/pyfonts.git
```

<br><br>

# Quick start

```python
from pyfonts import load_font
import matplotlib.pyplot as plt

# load font
font = load_font(
    font_url="https://github.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf"
)

# check how the font looks on a minimalist example
fig, ax = plt.subplots(figsize=(10, 6))
ax.text(
    x=0.5,
    y=0.5,
    s=f"What an easy way to load fonts, isn't it?",
    font=font,
    fontsize=20,
    ha="center",
)
plt.show()
```

![output of quick start](https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/img/quickstart.png?raw=true)

<br><br>

# How to find fonts?

### Google font

There are many fonts available on the web. The **easiest way** to find one is to follow these steps:

- Browse [Google Font website](https://fonts.google.com/) to find a font that you like. Let's say you want to use [Amaranth](https://fonts.google.com/specimen/Amaranth?query=amaranth).
- Go to [Google font github repository](https://github.com/google/fonts) and type the name of your desired font in the search bar. We find that Urbanist font file in **Bold** is named `https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf`.
- copy the url and add `?raw=true` at the end, which gives us `https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf?raw=true`
- and that's it! Just pass this to `load_font()` to use it in your matplotlib charts

```python
from pyfonts import load_font
import matplotlib.pyplot as plt

font = load_font(
    font_url="https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf?raw=true"
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.text(
    x=0.5,
    y=0.5,
    s=f"Congrats, you now have a cool font!",
    font=font,
    fontsize=20,
    ha="center",
)
plt.show()
```

For the url to be readable by `PyFonts` when using a Github url, it must be in one of (the following 3 urls are completely equivalent):

- `https://github.com/google/fonts/blob/main/apache/ultra/Ultra-Regular.ttf?raw=true`
- `https://github.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf`
- `https://raw.githubusercontent.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf`

The **recommended** is the first (`https://github.com/google/fonts/blob/main/apache/ultra/Ultra-Regular.ttf?raw=true`) because you just need to add `?raw=true` after the end of the Github url.

### Other places for fonts

Github is the ideal place to find fonts under a free licence. You can find many fonts on the web. Just make sure that the licence of the font allows you to use it in your project.

You can find other fonts at:

- [Awesome fonts](https://github.com/brabadu/awesome-fonts)
- [Nerd fonts](https://github.com/ryanoasis/nerd-fonts)

<br><br>

# PyFonts and Matplotlib

### How it works

In order to work with any font, `PyFonts` creates a temporary file and uses this file to create a [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties) object. Once the object has been created with your font, the program deletes the temporary file as it no longer needs it.

### Different weight and style

When you load a font, **you don't load all its extensions**: bold, italic, thin etc, but only the one from the url. If you want to be able to use a font and its **bold** version, for example, you need to load both fonts:

```python
from pyfonts import load_font
import matplotlib.pyplot as plt

font = load_font(
    font_url="https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Regular.ttf?raw=true"
)
bold_font = load_font(
    font_url="https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf?raw=true"
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.text(
    x=0.5,
    y=0.5,
    s=f"Congrats, you now have a cool font!",
    font=font,
    fontsize=20,
    ha="center",
)
ax.text(x=0.5, y=0.3, s=f"And now it's bold", font=bold_font, fontsize=20, ha="center")
plt.show()
```

![combine regular and bold font](https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/img/change_weight.png?raw=true)

<br><br>

# Other feature: download a font locally

If for some reason you want to store the fonts you're working with, simply use the `download_font()` function. It just needs the arguments `font_url` (as described above) and `destination_path` (where you want to store them, by default in the current directory).

You can suppress the output message by adding `verbose=False` to it.

```python
from pyfonts import download_font

download_font(
    font_url="https://github.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf",
    destination_path="/Users/josephbarbier/Desktop/myfont.ttf",  # optional
)
```

`Font installed at: /Users/josephbarbier/Desktop/myfont.ttf`

<br><br>
