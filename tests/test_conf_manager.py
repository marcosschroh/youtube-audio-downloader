import os
import unittest

from sound_downloader.conf_manager import ConfManager


class TestConfManager(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONF_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "conf.yml")
    EXPECTES_RESULTS = {
        "links": [
            "https://www.youtube.com/watch?v=hTWKbfoikeg",
            "https://www.youtube.com/watch?v=ygYYOeVoVgk",
            "https://www.youtube.com/watch?v=qYzY25b_uek"
        ],
        "audio_formats": ['m4a', 'mp4', 'mp3', 'webm', 'ogg', 'wma']
    }

    def test_get_conf(self):
        conf = ConfManager.get_conf(self.CONF_FILE_PATH)
        self.assertEqual(
            conf.links, self.EXPECTES_RESULTS.get('links'))
        self.assertEqual(
            conf.audio_formats,
            self.EXPECTES_RESULTS.get('audio_formats')
        )
