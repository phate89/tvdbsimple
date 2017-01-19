# -*- coding: utf-8 -*-

"""
This test suite checks the methods of tvdbsimple.

Use the following command to run all the tests:
    python -m unittest discover tests

"""
import os
"""
Either place your API_KEY in the following constant:
"""
API_KEY = os.environ.get('TVDB_API_KEY', '')
USER = os.environ.get('TVDB_USER', '')
USER_KEY = os.environ.get('TVDB_USER_KEY', '')

"""
or include it in a keys.py file.
"""
try:
    from .keys import *
except ImportError:
    pass
