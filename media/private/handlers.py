from . import BaseHandler
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class Mp3Tags(BaseHandler):
    _handles = [MP3.__name__, AIFF.__name__]

    @staticmethod
    def get_value(track, tag_key):
        return track.get(tag_key).text[0]

    @staticmethod
    def set_value(track, tag_key, value):
        track.get(tag_key).text[0] = unicode(value)


class Mp4Tags(BaseHandler):
    _handles = [MP4.__name__]

    @staticmethod
    def get_value(track, tag_key):
        return track.get(tag_key)[0]

    @staticmethod
    def set_value(track, tag_key, value):
        track.get(tag_key)[0] = unicode(value)
