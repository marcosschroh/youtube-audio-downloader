"""Command Line Tool"""
import click

from sound_downloader.arguments_parser import validate_config_file, \
 validate_target
from sound_downloader.downloader import YoutubeAudioDownloader


@click.command()
@click.option(
        "--conf", callback=validate_config_file,
        help="Path to file that contains the youtube links")
@click.option(
        "--destiny", callback=validate_target,
        default=".", help="Path to save the audios.",
        type=str)
def main(conf, destiny):
    downloader = YoutubeAudioDownloader(conf, path_to_save=destiny)
    downloader.download_audios()


if __name__ == "__main__":
    main()
