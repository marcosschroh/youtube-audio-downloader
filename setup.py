#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for youtube-audio-downloader."""

from setuptools import setup

setup(
    name="youtube-audio-downloader",
    version="1.1",
    description="Download audio from YouTube",
    keywords=["youtube-downloader", "downloader", "YouTube", "youtube", "download", "audio"],
    author="marcosschroh",
    author_email="marcos.06sch@gmail.com",
    url="https://github.com/marcosschroh/youtube-audio-downloader",
    download_url="https://github.com/marcosschroh/youtube-audio-downloader.git",
    install_requires=[
        "youtube-dl==2016.5.16",
        "pafy==0.5.0"
    ],
    scripts=["scripts/sound-down"],
    packages=["sound_downloader"],
    license='GPLv3'
)
