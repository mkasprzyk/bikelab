#!/usr/bin/env python
import shutil
import os

from cefpython3 import cefpython


workspace = os.getcwd()

cefpython_path = os.path.dirname(cefpython.__file__)

locales_path = os.path.join(workspace, 'dist', 'locales')
dist_path = os.path.join(workspace, 'dist')

pak_list = [
    'cef.pak',
    'cef_100_percent.pak',
    'cef_200_percent.pak',
    'cef_extensions.pak'
]

pak_lang_list = [
    'en-US.pak'
]

for pak in pak_list:
    pak_path = os.path.join(cefpython_path, pak)
    print("Copy {} -> {}".format(pak_path, dist_path))
    shutil.copy(
        pak_path,
        dist_path
    )

if not os.path.exists(locales_path):
    os.mkdir(locales_path)

for pak_lang in pak_lang_list:
    pak_lang_path = os.path.join(cefpython_path, 'locales', pak_lang)
    print("Copy {} -> {}".format(pak_lang_path, locales_path))
    shutil.copy(
        pak_lang_path,
        locales_path
    )
