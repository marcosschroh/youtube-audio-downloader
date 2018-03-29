import os
import shutil
import unittest

from sound_downloader.downloader import YoutubeAudioDownloader


class TestDownloader(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TARGET_FOLDER = os.path.join(BASE_DIR, "downloads")
    TARGET_FOLDER_WITH_AUDIOS = os.path.join(BASE_DIR, "not_override")
    CONF_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "conf.yml")

    def setUp(self):
        os.makedirs(self.TARGET_FOLDER)

    @staticmethod
    def _get_downloader(conf_file, target_folder):
        return YoutubeAudioDownloader(
            path_file=conf_file,
            path_to_save=target_folder
        )

    def test_download_audios(self):
        downloader = self._get_downloader(
            self.CONF_FILE_PATH, self.TARGET_FOLDER)

        downloader.download_audios()
        self.assertEqual(len(os.listdir(self.TARGET_FOLDER)), 3)

    def test_download_audios_not_override(self):
        downloader = self._get_downloader(
            self.CONF_FILE_PATH, self.TARGET_FOLDER_WITH_AUDIOS)

        downloader.download_audios()
        self.assertEqual(len(os.listdir(self.TARGET_FOLDER_WITH_AUDIOS)), 3)

    def tearDown(self):
        shutil.rmtree(self.TARGET_FOLDER)
