import types
import mutagen
from media.private import tags, repository


class Track(object):
    __track = None
    __tags = None

    def __init__(self, abs_path):
        track_obj = mutagen.File(abs_path)
        if isinstance(track_obj, types.NoneType):
            raise ImportError("The file '" + abs_path + "' cannot be loaded")

        self.__track = track_obj
        self.__tags = repository.TagsRepository(track_obj)

    def get_tags(self):
        return self.__tags

    def save(self):
        self.__track.save()

    def get_tag(self, tag):
        return self.__tags.get(tag)

    def artist(self, name=None):
        tag = self.get_tag(tags.Artist)
        if name is None:
            return tag.get()

        tag.set(name)

        return name

    def title(self, name=None):
        tag = self.get_tag(tags.Title)
        if name is None:
            return tag.get()

        tag.set(name)

        return name
