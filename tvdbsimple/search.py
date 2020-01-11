# -*- coding: utf-8 -*-

"""
This module implements the Search functionality of TheTVDb API.
Allows to search for tv series in the db.

See [Search API section](https://api.thetvdb.com/swagger#!/Search)
"""

import deprecation
from . import __version__
from .base import TVDB


class Search(TVDB):
    """
    Class that allow to search for series with filters.
    """
    _BASE_PATH = 'search'
    _URLS = {
        'series': '/series',
        'series_params': '/series/params'
    }

    def tvseries(self, name='', imdbId='', zap2itId='', language=''):
        """
        Search series with the information provided.

        You can set `name` to search for a series with that name. You can set `imdbId`
        to search a series with the provided imdb id. You can set `zap2itId`
        to search a series with the provided zap2it id. You can set `language` to
        retrieve the results with the provided language.

        Returns a list series with basic information that matches your search.

        For example

            #!python
            >>> import tvdbsimple as tvdb
            >>> tvdb.KEYS.API_KEY = 'YOUR_API_KEY'
            >>> search = tvdb.Search()
            >>> reponse = search.tvseries("doctor who 2005")
            >>> search.series[0]['seriesName']
            'Doctor Who (2005)'

        """
        res = self._series(name, imdbId, zap2itId, language)
        self._set_attrs_to_values({'series': res})
        return res

    # pylint: disable=undefined-variable
    @deprecation.deprecated(deprecated_in="1.0.7", removed_in="1.1.0", current_version=__version__,
                            details="Use the tvseries function instead")
    def series(self, name='', imdbId='', zap2itId='', language=''):
        """
        Search series with the information provided. Deprecated since 1.0.7
        """
        res = self._series(name, imdbId, zap2itId, language)
        self._set_attrs_to_values({'series': res})
        return res

    def _series(self, name='', imdbId='', zap2itId='', language=''):

        path = self._get_path('series')

        filters = {}
        if name:
            filters['name'] = name
        if imdbId:
            filters['imdbId'] = imdbId
        if zap2itId:
            filters['zap2itId'] = zap2itId

        self._set_language(language)
        return self._GET(path, params=filters)

    def tvseries_params(self):
        """
        Return the available search params.

        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        res = self._tvseries_params()
        self._set_attrs_to_values({'series_params': res})
        return res

    # pylint: disable=undefined-variable
    @deprecation.deprecated(deprecated_in="1.0.7", removed_in="1.1.0", current_version=__version__,
                            details="Use the tvseries_params function instead")
    def series_params(self):
        """
        Return the available search params. Deprecated since 1.0.7
        """
        res = self._tvseries_params()
        self._set_attrs_to_values({'series_params': response})
        return res

    def _tvseries_params(self):
        path = self._get_path('series_params')

        return self._GET(path)
