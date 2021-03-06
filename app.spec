# -*- mode: python -*-
import sys
import os

sys.path.append(os.path.join(os.getcwd()))
import settings
import utils

block_cipher = None
cef_resources = settings.cef_settings['resources_dir_path']

datas=[
	('./ui', 'ui'),
	('%s/subprocess' % utils.get_cefpython_path(), '.'),
	('%s/icudtl.dat' % cef_resources, settings.resources),
	('%s/natives_blob.bin' % cef_resources, settings.resources),
	('%s/cef.pak' % cef_resources, settings.resources),
	('%s/cef_100_percent.pak' % cef_resources, settings.resources),
	('%s/cef_200_percent.pak' % cef_resources, settings.resources),
	('%s/cef_extensions.pak' % cef_resources, settings.resources),
	(settings.locales_src, settings.locales_dst)
]

#TODO: Chromium Embedded Framework is duplicated and paths are ugly
if sys.platform == 'darwin':
    datas.append(
        ('%s/%s/Chromium Embedded Framework' %
        (utils.get_cefpython_path(), settings.framework), settings.framework)
    )

a = Analysis(['app.py'], datas=datas, cipher=block_cipher)

pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='bikelab',
          debug=False,
          strip=False,
          upx=True,
          console=False )
