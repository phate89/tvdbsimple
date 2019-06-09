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

    here = path.join(path.abspath(path.dirname(__file__)), fname)
    txt = ''
    if (path.isfile(here)):
        # Get the long description from the README file
        with open(here, encoding='utf-8') as f:
            txt= f.read()
    return txt

setup(
    name = 'tvdbsimple',
    version = '1.0.6',
    author = 'phate89',
    author_email = 'phates89@gmail.com',
    description = 'A Python wrapper for TheTVDb Database API v2',
    keywords = 'show series seasons tv database tvdb wrapper thetvdb api',
    url = 'https://github.com/phate89/tvdbsimple',
    download_url = 'https://github.com/phate89/tvdbsimple/tarball/1.0.6',
    packages = ['tvdbsimple'],
    license='GPLv3',
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
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ],
)
