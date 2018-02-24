import tags
import handlers
import inspect


class HandlersRepository(object):
    """ Repository that stores all the possible handlers """
    __repository = {}
    __loaded = False

    @staticmethod
    def _check_member(obj):
        return inspect.isclass(obj) \
               and issubclass(obj, handlers.BaseHandler) \
               and obj.__name__ != handlers.BaseHandler.__name__

    @classmethod
    def __load(cls):
        if len(cls.__repository) > 0:
            return

        for handler_tuple in inspect.getmembers(handlers, predicate=cls._check_member):
            handler = handler_tuple[1]
            if issubclass(handler, handlers.BaseHandler):
                for track_format in handler.what_can_handle():
                    cls.__repository[track_format] = handler

        cls.__loaded = True

    @classmethod
    def get_handler(cls, track):
        if not cls.__loaded:
            cls.__load()

        track_format = track.__class__.__name__
        if track_format not in cls.__repository:
            raise LookupError("Could not find a handle for the '" + track_format + "' format")

        return cls.__repository[track_format]


class TagsRepository(object):
    """ Tag repository specific to a track that stores that track's tag objects """
    __repository = {}

    @staticmethod
    def _check_member(obj):
        return inspect.isclass(obj) \
               and issubclass(obj, tags.BaseTag) \
               and obj.__name__ != tags.BaseTag.__name__

    def __load(self, track):
        handler = HandlersRepository.get_handler(track)

        for tag_tuple in inspect.getmembers(tags, predicate=TagsRepository._check_member):
            tag = tag_tuple[1]
            if issubclass(tag, tags.BaseTag):
                self.__repository[tag.name()] = tag(track, handler)

    def __init__(self, track):
        """ TagsRepository constructors """
        self.__load(track)

    def __iter__(self):
        return self.__repository.iteritems()

    def get_repository(self):
        return self.__repository

    def get(self, tag_cls):
        """ Return the tag handler """
        tag_name = tag_cls.name()
        if tag_name not in self.__repository:
            raise IndexError("Cannot find the request tag")

        return self.__repository[tag_name]
