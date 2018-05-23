# SIMPLE YOUTUBE AUDIO DOWNLOADER

## Based on [PAFY](https://github.com/mps-youtube/pafy)

## Features

* Download multiple songs from youtube.
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
  --conf FILE          Path to conf file
  --destiny PATH TO SAVE  Path to save the audios.

```

### Comands Examples

```sh
sound-down --conf example_conf.yml
sound-down --conf example_conf.yml --destiny /home/my_user/music/
```

### File Conf Example

[conf example](https://github.com/marcosschroh/youtube-audio-downloader/blob/master/examples/conf.yml)


### Configuration:


|    Options             |  Description                | Type  | Default |
|:----------------------:|:---------------------------:|:-----:|:-------:|
| youtube-links          | Youtube Links               | array |   []    |
| audio-formats-priority | Priority of audio formats * | array |  ['m4a', 'mp4', 'mp3', 'webm', 'ogg', 'wma'] |
| show-download-progress | Show the % of downloading per link  |  bool |   true  |
| overrride-audios       | Whether override audios that already exist in the Save Folder * | bool |  false  |




* Audio Priority: Always try to get the best audio based on format and quality. With the default conf will try to get the best audio for m4a format, if does not exist will try to get the best for mp4 and so on.

* Override: If you want to download a sound and it already exists in the folder that you have specified to place it, the audio will be override or not according to the value of `overrride-audios`.


### TODO

1. Show audio name or link in downloading process.
2. Maybe rethink using asyncio?
3. Maybe add a UI?