#!C:\Users\tireilly\Documents\GitHub\PythonHello\helloPython\HelloPy1\HelloPy1\foo\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==6.0.2','console_scripts','easy_install'
__requires__ = 'setuptools==6.0.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('setuptools==6.0.2', 'console_scripts', 'easy_install')()
    )
