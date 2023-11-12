# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['SquarePixel.py'],
    pathex=['SquarePixels/uimanagement/:SquarePixels/tests/:SquarePixels/terraingen/:SquarePixels/soundmanagement/:SquarePixels/render/:SquarePixels/player/:SquarePixels/multiplayer/:SquarePixels/game/:SquarePixels/enemymanagement/:SquarePixels/eastereggs/:SquarePixels/account_mannagement/:SquarePixels/:'],
    binaries=[],
    datas=[],
    hiddenimports=['SquarePixels'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Square Pixel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Recources\\PE EXE file compile recources\\icons scalable.ico'],
)
