 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import pafy
import csv
import argparse


class YoutubeVideoDownloader(object):
    PATH_TO_SAVE = "."

    def __init__(self, path_to_save=None):
        self.path_to_save = path_to_save or self.PATH_TO_SAVE
        self.link_list = []

    def process_csv_file(self, path_file):
        with open(path_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                link = row[0]
                self.link_list.append(link)

    def download_videos(self):
        for link in self.link_list:
            video = pafy.new(link)
            bestaudio = video.getbestaudio()
            bestaudio.download(quiet=False, filepath=self.path_to_save)


def set_arg_parser():
    parser = argparse.ArgumentParser(description="Youtube Audio Downloader")
    parser.add_argument("-f", metavar='FILE', type=str, dest="path_file",
        help="Path to file that contains the youtube links")
    parser.add_argument("-p", metavar='PATH TO SAVE', type=str, dest="path_to_save",
        default=".", help="Path to save the audios.")
    parser.add_argument("-o", metavar='OVERRIDE', type=str, dest="override_songs",
        default="yes", help="Override the existing songs?")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = set_arg_parser()
    path_file = args.path_file
    path_to_save = args.path_to_save
    youtube_downloader = YoutubeVideoDownloader(path_to_save=path_to_save)
    youtube_downloader.process_csv_file(path_file)
    youtube_downloader.download_videos()
