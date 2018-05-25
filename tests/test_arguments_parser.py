import os
import unittest
from click import BadParameter as BadParameterException

from sound_downloader.arguments_parser import validate_config_file, \
 validate_target


class TestParserUtilitis(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONF_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "conf.yml")
    INVALID_FILE = os.path.join(BASE_DIR, "example.py")

    def setUp(self):
        with open(self.INVALID_FILE, 'w') as _:
            pass

    def test_validate_target(self):
        """
        Validate Path Folder to store the downloaded audios.
        """
        path = validate_target('', 'destiny', self.BASE_DIR)
        self.assertEqual(self.BASE_DIR, path)

    def test_validate_file(self):
        self.assertEqual(
            validate_config_file('', 'file', self.CONF_FILE_PATH),
            self.CONF_FILE_PATH
        )

    def test_validate_file_invalid_extesion(self):
        with self.assertRaises(BadParameterException):
            validate_config_file('', 'file', self.INVALID_FILE)

    def test_validate_file_does_not_exist(self):
        with self.assertRaises(BadParameterException):
            validate_config_file('', 'file', 'example.txt')

    def tearDown(self):
        os.remove(self.INVALID_FILE)
