from abc import abstractmethod
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class BaseHandler(object):
    _handles = []

    @classmethod
    def what_can_handle(cls):
        return cls._handles

    @classmethod
    def can_handle(cls, track):
        track_type = track.__class__.__name__
        if track_type in cls._handles:
            return True

        return False

    @staticmethod
    @abstractmethod
    def get_value(track, tag_key):
        pass

    @staticmethod
    @abstractmethod
    def set_value(track, tag_key, value):
        pass


class Mp3Tags(BaseHandler):
    _handles = [MP3.__name__, AIFF.__name__]

    @staticmethod
    def get_value(track, tag_key):
        obj = track.get(tag_key)
        return obj.text[0]

    @staticmethod
    def set_value(track, tag_key, value):
        pass


class Mp4Tags(BaseHandler):
    _handles = [MP4.__name__]

    @staticmethod
    def get_value(track, tag_key):
        obj = track.get(tag_key)
        return obj[0]

    @staticmethod
    def set_value(track, tag_key, value):
        pass
