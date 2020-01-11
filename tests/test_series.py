# -*- coding: utf-8 -*-

"""
test suite checks the methods of the series class of tvdbsimple.
"""

import unittest
import tvdbsimple as tvdb

if not tvdb.keys.API_KEY:
    from tests import API_KEY
    tvdb.keys.API_KEY = API_KEY

"""
Constants
"""
TV_ID = 78804
TV_NAME = 'Doctor Who (2005)'


class SeriesTestCase(unittest.TestCase):
    def test_series_info(self):
        tvid = TV_ID
        name = TV_NAME
        series = tvdb.Series(tvid)
        series.info()
        self.assertEqual(series.seriesName, name)   # pylint: disable=no-member

    def test_series_actors(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.actors()
        self.assertTrue(hasattr(series, 'actors'))

    def test_series_episodes(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.Episodes.all()
        self.assertTrue(hasattr(series.Episodes, 'episodes'))

    def test_series_posters(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.Images.poster()
        self.assertTrue(hasattr(series.Images, 'poster'))

    def test_series_fanarts(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.Images.fanart()
        self.assertTrue(hasattr(series.Images, 'fanart'))

    def test_series_series(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.Images.series()
        self.assertTrue(hasattr(series.Images, 'series'))

    def test_series_season(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.Images.season()
        self.assertTrue(hasattr(series.Images, 'season'))

    def test_series_seasonwide(self):
        tvid = TV_ID
        series = tvdb.Series(tvid)
        series.Images.seasonwide()
        self.assertTrue(hasattr(series.Images, 'seasonwide'))
