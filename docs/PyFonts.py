import streamlit as st
import matplotlib.pyplot as plt
from pyfonts import load_font

from utils import st_spacing, read_readme_section
from ui import st_header, st_footer

plt.rcParams["figure.dpi"] = 300

st_header()
st_spacing(3)

font_url = st.text_input(
    "Enter a url to a font",
    value="https://github.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf",
)
st.code(
    f"""
   import matplotlib.pyplot as plt
   from pyfonts import load_font

   font = load_font(
      font_url="{font_url}"
   )

   fig, ax = plt.subplots()
   ax.text(
      x=0.5, y=0.5,
      s="This font looks pretty cool!",
      font=font, fontsize=15, ha="center"
   )
   plt.show()
   """
)

run_code = st.button("Run code")
if run_code:
    try:
        font = load_font(font_url=font_url)

        fig, ax = plt.subplots()
        ax.text(
            x=0.5,
            y=0.5,
            s="This font looks pretty cool!",
            font=font,
            fontsize=15,
            ha="center",
        )
        st.pyplot(fig)
    except:
        st.error("You URL seems invalid.")
st_spacing(3)


st.markdown("## Install PyFonts")
with st.expander("Installation"):
    readme_content = read_readme_section("# Installation")
    st.markdown(readme_content)
st_spacing(3)


st.markdown("## How to find fonts?")
with st.expander("Find fonts"):
    readme_content = read_readme_section("# How to find fonts?")
    st.markdown(readme_content)
st_spacing(3)

st.markdown("## Change weight and style")
with st.expander("Select a weight and/or style"):
    readme_content = read_readme_section("# PyFonts and Matplotlib", end_at="![")
    st.markdown(readme_content)
    st.image("img/change_weight.png")
st_spacing(3)

st.markdown("## Download a font locally")
with st.expander("Download a font"):
    readme_content = read_readme_section("# Other feature: download a font locally")
    st.markdown(readme_content)
st_spacing(3)

st_spacing(10)
st_footer()
