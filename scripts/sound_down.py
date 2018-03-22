"""Command Line Tool"""
import click

from sound_downloader.arguments_parser import validate_file, \
 validate_target
from sound_downloader.downloader import YoutubeAudioDownloader


@click.command()
@click.option(
        "--file", callback=validate_file,
        help="Path to file that contains the youtube links")
@click.option(
        "--destiny", callback=validate_target,
        default=".", help="Path to save the audios.",
        type=str)
def main(file, destiny):
    downloader = YoutubeAudioDownloader(file, path_to_save=destiny)
    downloader.download_audios()


if __name__ == "__main__":
    main()