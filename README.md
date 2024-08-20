# PyFonts

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="pyfonts logo" align="right" width="200px"/>

A simple way to load fonts for matplotlib.

Check out [the online documentation](https://python-graph-gallery.com/pyfonts/).

<br><br>

# Installation

You can install `pyfonts` directly from PyPI with:

```
pip install pyfonts
```

(not recommended) Alternatively you can install the **development version** with:

```
pip install git+https://github.com/JosephBARBIERDARNAL/pyfonts.git
```

<br><br>

# Quick start

```python
from pyfonts import load_font
import matplotlib.pyplot as plt

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

# Usage guide

Check out [the online documentation](https://python-graph-gallery.com/pyfonts/).

<br><br>

# Contributions

Contributions (and feedback) are welcome.

### TODO features:

- check the [issues](https://github.com/JosephBARBIERDARNAL/pyfonts/issues) for ideas
- suggest something (:

### Installation for contributions

_Follow the steps below for your OS._

1. **Fork the Repository:**
   Fork this repository to your GitHub account.

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/pyfonts.git
   cd pyfonts
   ```

3. **Set Up a Virtual Environment:**

   - **Mac/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

5. **Create a Feature Branch:**

   ```bash
   git checkout -b feature-name
   ```

6. **Start Coding!**

<br><br><br>
