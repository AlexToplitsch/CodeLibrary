# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['login.py'],
             pathex=['D:\\python\\Projekte\\Knapp_Apprentice_Training'],
             binaries=[],
             datas=[],
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
          name='KAT',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\python\\Projekte\\Lehrlingsdatenbank\\V1.1.3\\Knapp_Apprentice_Training\\_Symbole\\UsedSymbols\\school_bell_icon_175715.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='KAT')
