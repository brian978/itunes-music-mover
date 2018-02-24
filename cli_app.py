import os
from wrapper import prompt
from media import Track
from filesystem import resolve_path

abs_path = resolve_path(prompt("Absolute path of the file: "))
if not os.path.isfile(abs_path):
    print "The provided file path is invalid"
    quit(-1)

track = Track(os.path.expanduser(abs_path))

""" Update the tags """
track.artist(prompt("Artist [" + track.artist() + "]: ", track.artist()))
track.title(prompt("Artist [" + track.title() + "]: ", track.title()))
track.save()
