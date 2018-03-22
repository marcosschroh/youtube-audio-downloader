import os
import unittest
from click import BadParameter as BadParameterException

from sound_downloader.arguments_parser import validate_file, \
 validate_target


class TestParserUtilitis(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.csv")
    TXT_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.txt")
    JSON_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.json")
    INVALID_FILE = os.path.join(BASE_DIR, "example.py")

    def setUp(self):
        open(self.INVALID_FILE, 'w')

    def test_validate_target(self):
        """
        Validate Path Folder to store the downloaded audios.
        """
        path = validate_target('', 'destiny', self.BASE_DIR)
        self.assertEqual(self.BASE_DIR, path)

    def test_validate_file(self):
        self.assertEqual(
            validate_file('', 'file', self.CSV_FILE_PATH),
            self.CSV_FILE_PATH
        )
        self.assertEqual(
            validate_file('', 'file', self.TXT_FILE_PATH),
            self.TXT_FILE_PATH
        )
        self.assertEqual(
            validate_file('', 'file', self.JSON_FILE_PATH),
            self.JSON_FILE_PATH
        )

    def test_validate_file_invalid_extesion(self):
        with self.assertRaises(BadParameterException):
            validate_file('', 'file', self.INVALID_FILE)

    def test_validate_file_does_not_exist(self):
        with self.assertRaises(BadParameterException):
            validate_file('', 'file', 'example.txt')

    def tearDown(self):
        os.remove(self.INVALID_FILE)
