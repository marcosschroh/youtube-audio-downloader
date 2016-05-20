#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for youtube-audio-downloader."""

from setuptools import setup

setup(
    name='youtube-audio-downloader',
    packages=['youtube-audio-downloader'],
    scripts=['scripts/ytdl'],
    version='1.0',
    description="Download audio from YouTube",
    keywords=["youtube-downloader", "downloader", "YouTube", "youtube", "download", "audio"],
    author="marcosschroh",
    author_email="marcos.06sch@gmail.com",
    url="",
    download_url="",
    install_requires=[
        "youtube-dl==2016.5.16",
        "pafy==0.5.0"
    ],
    license='GPLv3'
)
