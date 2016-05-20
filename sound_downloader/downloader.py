 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import pafy
from .file_manager import FileManager


class YoutubeAudioDownloader(object):
    PATH_TO_SAVE = "."

    def __init__(self, path_file, path_to_save=None):
        self.path_file = path_file
        self.path_to_save = path_to_save or self.PATH_TO_SAVE

    @staticmethod
    def _get_links(path_file):
        return FileManager.get_links(path_file)

    def download_audios(self):
        links = self._get_links(self.path_file)
        for link in links:
            video = pafy.new(link)
            bestaudio = video.getbestaudio()
            bestaudio.download(quiet=False, filepath=self.path_to_save)
