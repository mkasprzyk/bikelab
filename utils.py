#!/usr/bin/env python
import sys
import os

from cefpython3 import cefpython


def get_cefpython_path():
    return os.path.dirname(cefpython.__file__)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = get_cefpython_path()
    return os.path.join(base_path, relative_path)
