import os
from wrapper import prompt
from media import Track
from media.private import BaseTag
from filesystem import resolve_path

abs_path = resolve_path(prompt("Absolute path of the file: "))
if not os.path.isfile(abs_path):
    print "The provided file path is invalid"
    quit(-1)

track = Track(os.path.expanduser(abs_path))

for tag, tag_obj in sorted(track.get_tags()):
    if isinstance(tag_obj, BaseTag):
        default_value = tag_obj.get()
        tag_obj.set(prompt("tag[" + default_value + "]: ", default_value))

""" Update the tags """
track.save()
