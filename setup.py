# -*- coding: utf-8 -*-

"""
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

def read(fname):

    here = path.abspath(path.dirname(__file__))

    txt = ''
    if (path.isfile(here)):
        # Get the long description from the README file
        with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
            txt= f.read()
    return txt

setup(
    name = 'tvdbsimple',
    version = '1.0.1',
    author = 'phate89',
    author_email = 'phates89@gmail.com',
    description = 'A Python wrapper for TheTVDb Database API v2',
    keywords = ['show', 'series', 'seasons', 'the tv database', 'tv database', 'tvdb', 
                'wrapper', 'database', 'thetvdb', 'api'],
    url = 'https://github.com/phate89/tvdbsimple',
    download_url = 'https://github.com/phate89/tvdbsimple/tarball/1.0.1',
    packages = ['tvdbsimple'],
    long_description=read('README.rst'),
    install_requires = ['requests'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities"
    ],
)
