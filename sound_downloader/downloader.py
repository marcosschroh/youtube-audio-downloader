# -*- coding: utf-8 -*-

import pafy
from .conf_manager import ConfManager


class YoutubeAudioDownloader(object):
    PATH_TO_SAVE = "."

    def __init__(self, path_file, path_to_save=None):
        self.path_file = path_file
        self.path_to_save = path_to_save or self.PATH_TO_SAVE

    def download_audios(self):
        conf = ConfManager.get_conf(self.path_file)

        links = conf.links
        audio_formats = conf.audio_formats

        for link in links:
            video = pafy.new(link)

            audios = [
                audio for audio in video.audiostreams if audio.extension in audio_formats]

            # if there are not audios according to the extensions continue
            # probably we need a logger
            if not audios:
                continue

            # sort the audios: first by extension and then for quality
            audios.sort(
                key=lambda a: (audio_formats.index(a.extension), int(a.quality.strip('k')) * -1))

            best_audio = audio[0]
            best_audio.download(quiet=False, filepath=self.path_to_save)
