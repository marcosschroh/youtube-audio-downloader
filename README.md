# SIMPLE YOUTUBE AUDIO DOWNLOADER

## Based on [PAFY](https://github.com/mps-youtube/pafy)

## Features

* Download multiple songs from youtube. Just give a .txt file or .csv file that contains the song's links.
* Works with Python 2.6+ and Python 3.3+.

### Installation

```sh
pip install youtube-audio-downloader
```

### Comand line usage

```sh
usage: sound-down [-h] -f FILE [-p PATH TO SAVE]

Youtube Audio Downloader

optional arguments:
  -h, --help       show this help message and exit
  -f FILE          Path to file that contains the youtube links
  -p PATH TO SAVE  Path to save the audios.

```

### Examples

```sh
sound-down -f example.txt
sound-down -f example.csv
sound-down -f example.csv -p /home/my_user/music/
```

### Notes:

* In .txt file put one link per line





