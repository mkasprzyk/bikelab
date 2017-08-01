#!/usr/bin/env python
import os
import sys

from utils import *


cef_settings = {}

cef_switches = {
    "ignore-gpu-blacklist": "true",
}

if sys.platform == 'darwin':
    framework = 'Chromium Embedded Framework.framework'
    resources = os.path.join(framework, 'Resources')
    cef_settings.update({
        "resources_dir_path": resource_path(resources),
        "framework_dir_path": resource_path(framework),
        "locales_dir_path": resource_path(resources),
    })
    locales_src = resource_path(os.path.join(resources, 'en.lproj'))
    locales_dst = resources
else:
    resources = '.'
    cef_settings.update({
        "resources_dir_path": resource_path(resources),
        "locales_dir_path": resource_path('locales'),
    })
    locales_src = resource_path('locales', 'en-US.pak')
    locales_dst = os.path.join('locales', 'en-US.pak')

if hasattr(sys, 'freeze'):
    UI_PATH = resource_path("ui")
else:
    UI_PATH = os.path.join(os.getcwd(), 'ui')
