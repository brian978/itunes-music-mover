import os
from shutil import copyfile
from metadata.tracks import Track


class Filesystem(object):
    @staticmethod
    def resolve_path(abs_path):
        if not isinstance(abs_path, str):
            return ""

        if abs_path[0] == "~":
            return os.path.join(os.path.expanduser("~/"), abs_path[2:])

        return abs_path


class Crawler(object):
    """ The class returns a list of files based on the given directory """
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
    """ The class handles the copy/move operations on the files """
    _dir = None

    @staticmethod
    def _get_track(abs_path):
        """ Returns a Track object """
        return Track(abs_path)

    @staticmethod
    def _format_filename(abs_path, track):
        """ Formats the filename """
        extension = os.path.splitext(abs_path)[1]

        return track.artist() + " - " + track.title() + extension

    def __init__(self, dst_dir):
        """ Crawler constructor """
        self._dir = Filesystem.resolve_path(dst_dir)

    def _check_dir(self):
        """ Check if the directory exists and creates it if it doesn't """
        if not os.path.isdir(self._dir):
            os.makedirs(self._dir)

    def _do_copy(self, src_full_path, dst_filename):
        """ Executes the copy operation """
        dst_file = os.path.join(self._dir, dst_filename)
        if os.path.isfile(dst_file):
            os.remove(dst_file)

        copyfile(src_full_path, dst_file)

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
                track = Mover._get_track(abs_path)
                dst_filename = self._format_filename(abs_path, track)

                self._do_copy(abs_path, dst_filename)
            except ImportError, e:
                errors.append({"import_error": e})
                continue

        print ("Processing done")

        if len(errors) > 0:
            print ("The copy encountered errors")

        return errors
