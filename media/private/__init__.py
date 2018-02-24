from abc import abstractmethod


class BaseTag(object):
    """ Base tag class """
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


class BaseHandler(object):
    """ Base handler class """
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
