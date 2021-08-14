from setuptools import setup

from ahk_binary import __version__

setup(
    name='ahk-binary',
    version=__version__,
    author_email='spencer.young@spyoung.com',
    author='Spencer Young',
    url="https://github.com/spyoungtech/ahk-binary",
    data_files=[('Scripts', ['AutoHotkey.exe'])],
    packages=['ahk_binary'],
    license="GNU General Public License v2 (GPLv2)",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
)