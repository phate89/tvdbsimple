# -*- coding: utf-8 -*-

"""
test suite checks the methods of the episode class of tvdbsimple.
"""

import unittest
import tvdbsimple as tvdb

if not tvdb.keys.API_KEY:
    from tests import API_KEY
    tvdb.keys.API_KEY = API_KEY

"""
Constants
"""
EP_ID = 1452931
EP_TITLE = 'Flesh and Stone (2)'

class EpisodeTestCase(unittest.TestCase):
    def test_episode_info(self):
        id = EP_ID
        name = EP_TITLE
        episode = tvdb.Episode(id)
        response = episode.info()
        self.assertEqual(episode.episodeName, name)

