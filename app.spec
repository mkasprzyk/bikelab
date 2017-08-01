# -*- mode: python -*-
import sys
import os

sys.path.append(os.path.join(os.getcwd()))
import settings

block_cipher = None

cefp = settings.get_cefpython_path()

a = Analysis(['app.py'],
             datas=[
               ('./ui', 'ui'),
               ('%s/icudtl.dat' % cefp, settings.resources),
               ('%s/natives_blob.bin' % cefp, settings.resources),
               ('%s/cef.pak' % cefp, '.'),
               ('%s/cef_100_percent.pak' % cefp, '.'),
               ('%s/cef_200_percent.pak' % cefp, '.'),
               ('%s/cef_extensions.pak' % cefp, '.'),
               (settings.locales_src, settings.locales_dst)
             ],
             cipher=block_cipher)

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
