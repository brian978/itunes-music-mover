import os
import mutagen
import types
from shutil import copyfile
from tags import Tags


class Crawler(object):
    _excluded = [".", "..", ".DS_Store"]
    _dir = None

    def __init__(self, src_dir):
        """ Crawler constructor """
        self._dir = os.path.expanduser(src_dir)

    def get_files(self):
        """ Returns a list of files (full path) """
        directory = os.path.abspath(self._dir)
        files = []

        for (dirpath, dirnames, filenames) in os.walk(directory):
            for filename in filenames:
                if filename not in [".DS_Store", "..", "."]:
                    files.append(os.path.join(dirpath, filename))

        return files


class Mover(object):
    _dir = None
    _tags = Tags()

    def __init__(self, dst_dir):
        """ Crawler constructor """
        if dst_dir[0] == "~":
            self._dir = os.path.join(os.path.expanduser("~/"), dst_dir[2:])
        else:
            self._dir = dst_dir

    def _get_track(self, abs_path):
        """ Returns the track file and updates the tags object with the track file """
        track = mutagen.File(abs_path)
        if isinstance(track, types.NoneType):
            raise ImportError("The file '" + abs_path + "' cannot be loaded")

        self._tags.track = track

        return track

    def _check_dir(self):
        if not os.path.isdir(self._dir):
            os.makedirs(self._dir)

    def _format_filename(self, abs_path):
        """ Formats the filename """
        extension = os.path.splitext(abs_path)[1]

        return self._tags.artist() + " - " + self._tags.title() + extension

    def _do_copy(self, src_file):
        """ Executes the copy operation """
        dst_file = os.path.join(self._dir, self._format_filename(src_file))
        if os.path.isfile(dst_file):
            os.remove(dst_file)

        copyfile(src_file, dst_file)

        return dst_file

    def copy_files(self, files):
        """ Copies the files to the new location """
        print("Processing " + str(len(files)) + " files")

        self._check_dir()  # check if dir exists and creates it if not

        errors = []

        for abs_path in files:
            if not os.path.isfile(abs_path):
                errors.append({"missing_file": abs_path})
                continue

            try:
                self._get_track(abs_path)
                self._do_copy(abs_path)
            except ImportError, e:
                errors.append({"import_error": e})
                continue

        print ("Processing done")

        if len(errors) > 0:
            print ("The copy encountered errors")

        return errors
