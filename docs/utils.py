import streamlit as st
import re


def read_readme_section(start_at, end_at="<br><br>"):
    with open("README.md") as file:
        content = file.read()

    # Find the starting point
    start_index = content.find(start_at)
    start_index += len(start_at)

    # Find the ending point
    end_index = content.find(end_at, start_index)
    if end_index == -1:
        end_index = len(content)

    # Extract the relevant section
    section = content[start_index:end_index].strip()

    # Remove any HTML tags (optional, depends on your needs)
    section = re.sub("<[^<]+?>", "", section)

    return section
