import sys
import yaml
import collections

Conf = collections.namedtuple(
    'Conf',
    'links audio_formats show_download_progress overrride_audios'
)


class ConfManager(object):

    DEFAULT_AUDIO_FORMATS = ['mp4', 'mp3', 'webm', 'm4a', 'ogg', 'wma']

    @classmethod
    def get_conf(cls, file_path):
        with open(file_path, 'r') as stream:
            try:
                conf = yaml.load(stream)
            except yaml.YAMLError as exc:
                sys.exit(exc)

        links = conf.get('youtube-links', [])
        audio_formats = conf.get(
            'audio-formats-priority',
            cls.DEFAULT_AUDIO_FORMATS
        )
        show_download_progress = conf.get('show-download-progress', True)
        overrride_audios = conf.get('overrride-audios', False)

        return Conf(
            links=links,
            audio_formats=audio_formats,
            show_download_progress=show_download_progress,
            overrride_audios=overrride_audios
        )
