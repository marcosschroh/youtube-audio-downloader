import os
import shutil
import unittest

from sound_downloader.downloader import YoutubeAudioDownloader


class TestParserUtilitis(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TARGET_FOLDER = os.path.join(BASE_DIR, os.pardir, "examples", "downloads")
    CSV_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.csv")

    def setUp(self):
        os.makedirs(self.TARGET_FOLDER)
        self.downloader = YoutubeAudioDownloader(
            path_file=self.CSV_FILE_PATH,
            path_to_save=self.TARGET_FOLDER
        )

    def test_download_audios(self):
        self.downloader.download_audios()
        self.assertEqual(len(os.listdir(self.TARGET_FOLDER)), 2)

    def tearDown(self):
        shutil.rmtree(self.TARGET_FOLDER)
