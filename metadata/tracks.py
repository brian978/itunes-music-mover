import tags
import repository


class Track(object):
    __track = None
    __tags = None

    def __init__(self, raw_track):
        self.__track = raw_track
        self.__tags = repository.TagsRepository(self.__track)

    def artist(self):
        return self.__tags.get(tags.Artist).get()

    def title(self):
        return self.__tags.get(tags.Title).get()
