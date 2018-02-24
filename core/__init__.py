import os


def resolve_path(abs_path):
    if not isinstance(abs_path, str):
        return ""

    if abs_path[0] == "~":
        return os.path.join(os.path.expanduser("~/"), abs_path[2:])

    return abs_path
