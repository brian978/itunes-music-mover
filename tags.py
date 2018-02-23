from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


class Tags(object):
    track = None

    @staticmethod
    def _format_unicode(data):
        """ Formats the data for a specific format"""
        return data.encode("utf8", "replace")

    def artist(self):
        """ Returns the artist name """
        tag_value = None

        if isinstance(self.track, MP3) or isinstance(self.track, AIFF):
            obj = self.track.get("TPE1")
            tag_value = obj.text[0]

        if isinstance(self.track, MP4):
            obj = self.track.get("\xa9ART")
            tag_value = obj[0]

        if tag_value is not None:
            return Tags._format_unicode(tag_value)

        raise NotImplementedError("Cannot extract the artist for the given audio file")

    def title(self):
        """ Returns the track title """
        tag_value = None

        if isinstance(self.track, MP3) or isinstance(self.track, AIFF):
            obj = self.track.get("TIT2")
            tag_value = obj.text[0]

        if isinstance(self.track, MP4):
            obj = self.track.get("\xa9nam")
            tag_value = obj[0]

        if tag_value is not None:
            return Tags._format_unicode(tag_value)

        raise NotImplementedError("Cannot extract the title for the given audio file")
