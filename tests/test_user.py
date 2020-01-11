# -*- coding: utf-8 -*-

"""
test suite checks the methods of the user class of tvdbsimple.
"""

import unittest
import sys
import tvdbsimple as tvdb

from tests import USER, USER_KEY
if not tvdb.keys.API_KEY:
    tvdb.keys.API_KEY = API_KEY  # pylint: disable=undefined-variable

"""
Constants
"""
SERIES_ID = "2738" + str(sys.version_info.major) + str(sys.version_info.minor)


class UserTestCase(unittest.TestCase):
    def test_user_info(self):
        user = tvdb.User(USER, USER_KEY)
        user.info()
        self.assertEqual(user.userName, USER)   # pylint: disable=no-member

    def test_user_favorites(self):
        user = tvdb.User(USER, USER_KEY)
        user.favorites()
        self.assertTrue(hasattr(user, 'favorites'))

    def test_user_add_favorite(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.add_favorite(SERIES_ID)
        self.assertTrue(SERIES_ID in response)

    def test_user_delete_favorite(self):
        user = tvdb.User(USER, USER_KEY)
        response = user.delete_favorite(SERIES_ID)
        self.assertTrue(SERIES_ID not in response)

    def test_user_ratings(self):
        user = tvdb.User(USER, USER_KEY)
        user.Ratings.all()
        self.assertTrue(hasattr(user.Ratings, 'ratings'))

    def test_user_add_rating(self):
        user = tvdb.User(USER, USER_KEY)
        user.Ratings.add('series', SERIES_ID, 8)

    def test_user_delete_rating(self):
        user = tvdb.User(USER, USER_KEY)
        user.Ratings.delete('series', SERIES_ID)
