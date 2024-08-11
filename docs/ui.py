import streamlit as st


def st_header():
    st.html(
        f"""
      <center><h1>PyFonts</h1></center>
      <center><h3>Try and Preview fonts for Matplotlib</h3></center>
      """
    )


def st_footer():
    st.html(
        f"""
      <center><a href='https://github.com/JosephBARBIERDARNAL/pyfonts'>Github</a> (give it a star ⭐)</center>
      <center>PyFonts, by <a href='https://barbierjoseph.com/'>Joseph Barbier</a></center>
      """
    )


def st_spacing(n: int):
    for _ in range(n):
        st.text("")
