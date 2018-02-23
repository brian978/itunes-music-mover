from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class Track(object):
    __track = None

    @staticmethod
    def _format_unicode(data):
        """ Formats the data for a specific format"""
        return data.encode("utf8", "replace")

    def __init__(self, track):
        self.__track = track

    def artist(self):
        """ Returns the artist name """
        tag_value = None

        if isinstance(self.__track, MP3) or isinstance(self.__track, AIFF):
            obj = self.__track.get("TPE1")
            tag_value = obj.text[0]

        if isinstance(self.__track, MP4):
            obj = self.__track.get("\xa9ART")
            tag_value = obj[0]

        if tag_value is not None:
            return Track._format_unicode(tag_value)

        raise NotImplementedError("Cannot extract the artist for the given audio file")

    def title(self):
        """ Returns the track title """
        tag_value = None

        if isinstance(self.__track, MP3) or isinstance(self.__track, AIFF):
            obj = self.__track.get("TIT2")
            tag_value = obj.text[0]

        if isinstance(self.__track, MP4):
            obj = self.__track.get("\xa9nam")
            tag_value = obj[0]

        if tag_value is not None:
            return Track._format_unicode(tag_value)

        raise NotImplementedError("Cannot extract the title for the given audio file")
