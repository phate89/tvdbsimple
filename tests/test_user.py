# -*- coding: utf-8 -*-

"""
test suite checks the methods of the user class of tvdbsimple.
"""

import unittest
import tvdbsimple as tvdb
import sys

from tests import USER, USER_KEY
if not tvdb.keys.API_KEY:
    tvdb.keys.API_KEY = API_KEY

"""
Constants
"""
SERIES_ID = "2738" + str(sys.version_info.major) + str(sys.version_info.minor)

class UserTestCase(unittest.TestCase):
    def test_user_info(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.info()
        self.assertEqual(user.userName, USER)

    def test_user_favorites(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.favorites()
        self.assertTrue(hasattr(user, 'favorites'))

    def test_user_add_favorite(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.add_favorite(SERIES_ID)
        self.assertTrue(SERIES_ID in response)

    def test_user_delete_favorite(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.delete_favorite(SERIES_ID)
        self.assertTrue(SERIES_ID  not in response)

    def test_user_favorites(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.Ratings.all()
        self.assertTrue(hasattr(user.Ratings, 'ratings'))

    def test_user_add_favorite(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.Ratings.add('series', SERIES_ID, 8)

    def test_user_delete_favorite(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.Ratings.delete('series', SERIES_ID)
