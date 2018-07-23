#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for youtube-audio-downloader."""

from setuptools import setup, find_packages

__version__ = "1.1.9"

setup(
    name="youtube-audio-downloader",
    version=__version__,
    description="Download audio from YouTube",
    keywords=["youtube-downloader", "downloader", "YouTube", "youtube", "download", "audio"],
    author="marcosschroh",
    author_email="schrohm@gmail.com",
    url="https://github.com/marcosschroh/youtube-audio-downloader",
    download_url="https://github.com/marcosschroh/youtube-audio-downloader.git",
    install_requires=[
        "youtube-dl==2017.11.15",
        "pafy==0.5.0",
        "click==6.7",
        "PyYAML==3.12"
    ],
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    entry_points='''
        [console_scripts]
        sound-down=sound_downloader.scripts.sound_down:main
    ''',
)
