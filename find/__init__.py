__all__ = ['dirs', 'files']


import os


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


def _iter_files(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for f in files:
            yield os.path.join(root, f)


def _iter_dirs(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for d in dirs:
            yield os.path.join(root, d)


def dirs(path, followlinks=False):
    """return a list of dirs"""
    return list(_iter_dirs(path, followlinks))


def files(path, followlinks=False):
    """return a list of files"""
    return list(_iter_files(path, followlinks))
