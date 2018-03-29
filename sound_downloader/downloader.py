# -*- coding: utf-8 -*-
import os

import pafy
from .conf_manager import ConfManager


class YoutubeAudioDownloader(object):
    PATH_TO_SAVE = "."

    def __init__(self, path_file, path_to_save=None):
        self.path_file = path_file
        self.path_to_save = path_to_save or self.PATH_TO_SAVE
        self.files_in_save_folder = os.listdir(self.path_to_save)
        self.links = []
        self.audio_formats = None
        self.show_download_progress = True
        self.overrride_audios = False

    def _get_best_audio(self, video):
        audios = [
            audio for audio in video.audiostreams
            if audio.extension in self.audio_formats
        ]

        # if there are not audios according to the extensions continue
        # probably we need a logger
        if not audios:
            return

        # sort the audios: first by extension and then for quality
        audios.sort(
            key=lambda a: (self.audio_formats.index(a.extension), int(a.quality.strip('k')) * -1))

        return audios[0]

    def _set_conf(self):
        conf = ConfManager.get_conf(self.path_file)
        self.links = conf.links
        self.audio_formats = conf.audio_formats
        self.show_download_progress = conf.show_download_progress
        self.show_download_progress = conf.show_download_progress
        self.overrride_audios = conf.overrride_audios

    def _should_not_override(self, filename):
        return not self.overrride_audios and filename in self.files_in_save_folder

    def download_audios(self):
        self._set_conf()

        for link in self.links:
            video = pafy.new(link)

            best_audio = self._get_best_audio(video)
            filename = best_audio.filename

            if not best_audio:
                # TODO: Add proper logger.
                continue

            if self._should_not_override(filename):
                # TODO: Add proper logger.
                continue

            best_audio.download(
                quiet=not self.show_download_progress,
                filepath=self.path_to_save
            )
