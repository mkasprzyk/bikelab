# -*- mode: python -*-

block_cipher = None

def get_cefpython_path():
    from cefpython3 import cefpython
    path = os.path.dirname(cefpython.__file__)
    return "%s%s" % (path, os.sep)

cefp = get_cefpython_path()
a = Analysis(['app.py'],
             datas=[
               ('%s/icudtl.dat' % cefp, '.'),
               ('%s/natives_blob.bin' % cefp, '.'),
             ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

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
