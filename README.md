# SIMPLE YOUTUBE AUDIO DOWNLOADER

## Based on [PAFY](https://github.com/mps-youtube/pafy)

## Features

* Download multiple songs from youtube. Just give a .txt, .json or .csv file that contains the song's links.
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

### Comands Examples

```sh
sound-down -f example.txt
sound-down -f example.csv
sound-down -f example.csv -p /home/my_user/music/
```

### File Examples

[json example](https://github.com/marcosschroh/youtube-audio-downloader/blob/master/examples/example.json)
[txt example](https://github.com/marcosschroh/youtube-audio-downloader/blob/master/examples/example.txt)
[csv example](https://github.com/marcosschroh/youtube-audio-downloader/blob/master/examples/example.csv)

### Notes:

* In .txt file put one link per line





