from distutils.core import setup
import py2exe

setup(windows = [{ "script": "FantaManager.py", "icon_resources": [(1, "FM.ico")]}])

