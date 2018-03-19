import os
import unittest

from sound_downloader.file_manager import FileManager


class TestFileManager(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.csv")
    TXT_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.txt")
    EXPECTES_RESULTS = expected_result = {
        "https://www.youtube.com/watch?v=hTWKbfoikeg",
        "https://www.youtube.com/watch?v=ygYYOeVoVgk"
    }

    def test_get_links_csv(self):
        links = FileManager.get_links(self.CSV_FILE_PATH)
        self.assertEqual(self.EXPECTES_RESULTS, links)

    def test_get_links_txt(self):
        links = FileManager.get_links(self.TXT_FILE_PATH)
        self.assertEqual(self.EXPECTES_RESULTS, links)
