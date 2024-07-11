from setuptools import setup, find_packages

setup(
    name="lazyfont",
    version="0.0.1",
    packages=find_packages(),
    description="A simple way to load fonts for matplotlib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/lazyfont/blob/main/README.md",
    install_requires=[
        "matplotlib"
    ],
)