# -*- mode: python -*-

block_cipher = None


a = Analysis(['server.py'],
             pathex=['D:\\Dropbox\\Dropbox\\Projects\\CataclysmLD'],
             binaries=[
                        ('.\\img\\','.\\img\\'),
                        ('.\\data\\','.\\data\\'),
                        ('.\\tilesets\\','.\\tilesets\\'),
                        ('.\\worlds\\default\\delete.me','.\\worlds\\default\\'),
             ],
             datas=[
                 ('.\\server.cfg', '.'),
                 ('.\\log\\delete.me', '.\\log'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='server',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='server')
