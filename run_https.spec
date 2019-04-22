# -*- mode: python -*-

block_cipher = None

data_files = [
    ('data', 'data'),
    ('lib', 'lib'),
    ('ssl', 'ssl'),
    ('config', 'config'),
    ('bes.sh', './'),
    ('pid.lock', './')
]


a = Analysis(['run_https.py'],
             pathex=['/root/ses/bes'],
             binaries=[],
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='bes',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bes')
