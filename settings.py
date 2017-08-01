#!/usr/bin/env python
import os
import sys

from cefpython3 import cefpython
from utils import *


def get_cefpython_path():
    path = os.path.dirname(cefpython.__file__)
    if sys.platform == 'darwin':
        path = os.path.join(path, "Chromium Embedded Framework.framework", "Resources")
    return path

cef_settings = {
    "resources_dir_path": resource_path('.'),
}

cef_switches = {
    "ignore-gpu-blacklist": "true",
}

if sys.platform != 'darwin':
    resources = '.'
    locales_src = os.path.join(get_cefpython_path(), 'locales', 'en-US.pak')
    locales_dst = os.path.join('locales', 'en-US.pak')
    cef_settings.update({
        "locales_dir_path": resource_path('locales'),
    })
else:
    resources = 'Resources'
    locales_src = os.path.join(get_cefpython_path(), 'en.lproj', 'locale.pak')
    locales_dst = os.path.join(resources, 'en.lproj', 'locale.pak')
    cef_settings.update({
        "framework_dir_path": resource_path('.'),
        "locales_dir_path": resource_path(resources),
    })

CORE_PATH = resource_path("core")
UI_PATH = resource_path("ui")

