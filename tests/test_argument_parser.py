import os
import unittest

from argparse import ArgumentParser

from sound_downloader.arguments_parser import validate_file, \
 validate_target


class TestParserUtilitis(unittest.TestCase):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.csv")
    TXT_FILE_PATH = os.path.join(BASE_DIR, os.pardir, "examples", "example.txt")
    INVALID_FILE = os.path.join(BASE_DIR, "example.py")
    PARSER = ArgumentParser()

    def setUp(self):
        open(self.INVALID_FILE, 'w')

    def test_validate_target(self):
        """
        Validate Path Folder to store the downloaded audios.
        """
        path = validate_target(self.PARSER, self.BASE_DIR)
        self.assertEqual(self.BASE_DIR, path)

    def test_validate_file(self):
        self.assertEqual(
            validate_file(self.PARSER, self.CSV_FILE_PATH), self.CSV_FILE_PATH)
        self.assertEqual(
            validate_file(self.PARSER, self.TXT_FILE_PATH), self.TXT_FILE_PATH)

    def test_validate_file_does_not_exist(self):
        with self.assertRaises(SystemExit):
            validate_file(self.PARSER, 'example.txt')

    def test_validate_file_invalid_extesion(self):
        with self.assertRaises(SystemExit):
            validate_file(self.PARSER, self.INVALID_FILE)

    def tearDown(self):
        os.remove(self.INVALID_FILE)
