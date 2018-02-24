from . import BaseTag
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.aiff import AIFF


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
