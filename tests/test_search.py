# -*- coding: utf-8 -*-

"""
test suite checks the methods of the search class of tvdbsimple.
"""

import unittest
import tvdbsimple as tvdb

if not tvdb.keys.API_KEY:
    from tests import API_KEY
    tvdb.keys.API_KEY = API_KEY

"""
Constants
"""
SRC_STR = 'doctor who 2005'
SRC_NAME = 'Doctor Who (2005)'


class SearchTestCase(unittest.TestCase):
    def test_search_series(self):
        src = SRC_STR
        name = SRC_NAME
        search = tvdb.Search()
        response = search.series(src)
        self.assertEqual(search.series[0]['seriesName'], name)
