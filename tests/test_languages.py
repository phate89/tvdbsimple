# -*- coding: utf-8 -*-

"""
test suite checks the methods of the languages class of tvdbsimple.
"""

import unittest
import tvdbsimple as tvdb

if not tvdb.keys.API_KEY:
    from tests import API_KEY
    tvdb.keys.API_KEY = API_KEY

"""
Constants
"""
LAN_ID = 7
LAN_NAME = 'English'

class LanguagesTestCase(unittest.TestCase):
    def test_language_info(self):
        id = LAN_ID
        name = LAN_NAME
        lan = tvdb.Languages()
        response = lan.language(id)
        self.assertEqual(response['englishName'], name)
        
    def test_language_all(self):
        id = LAN_ID
        name = LAN_NAME
        lan = tvdb.Languages()
        response = lan.all()
        self.assertTrue(hasattr(lan, 'all'))


