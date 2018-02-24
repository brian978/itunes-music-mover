from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class BaseTag(object):
    _keys = {}
    _tag_key = ""
    _track = None
    _handler = None

    @staticmethod
    def _encode(data):
        """ Formats the data for a specific format"""
        return data.encode("utf8", "replace")

    @classmethod
    def name(cls):
        return str(cls.__name__).lower()

    def __init__(self, track, handler):
        """ BaseTag constructor """
        self._track = track
        self._handler = handler
        self._tag_key = self._keys[track.__class__.__name__]

    def get(self):
        return BaseTag._encode(self._handler.get_value(self._track, self._tag_key))

    def set(self, value):
        return self._handler.set_value(self._track, self._tag_key, value)


class Artist(BaseTag):
    _keys = {
        MP3.__name__: "TPE1",
        AIFF.__name__: "TPE1",
        MP4.__name__: "\xa9ART",
    }


class Title(BaseTag):
    _keys = {
        MP3.__name__: "TIT2",
        AIFF.__name__: "TIT2",
        MP4.__name__: "\xa9nam",
    }
