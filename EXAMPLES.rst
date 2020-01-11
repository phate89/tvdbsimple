Examples
--------

Once you have the *tvdbsimple* package installed and a TheTVDb API key, you can start to play with the data.

First, import the library and assign your API_KEY.

.. code-block:: python

    >>> import tvdbsimple as tvdb
    >>> tvdb.KEYS.API_KEY = 'YOUR_API_KEY_HERE'

To communicate with TheTVDb API, create an instance of one of the object types, call one of the methods on the instance, and access the instance attributes.  Use keys to access the values of attributes that are dictionaries.  In this example, we create a series instance for 'Doctor Who (2015)' and determine the day of week airing and rating.

.. code-block:: python

    >>> show = tvdb.Series(78804)
    >>> response = show.info()
    >>> show.seriesName
    'Doctor Who (2005)'
    >>> show.airsDayOfWeek
    'Saturday'
    >>> show.siteRating
    9.4

We can also retrieve the list of series episodes with basic informations. In this example i will retrieve the title of the first episode.

.. code-block:: python

    >>> episodes = show.Episodes.all()
    >>> episodes[0]['episodeName']
    u'Rose'

And also get all the art types for the specific series. In this example i will get the resolution of the first poster.

.. code-block:: python

    >>> posters = show.Images.poster()
    >>> posters[0]['resolution']
    '680x1000'

We can get more detailed information about one single episode. In this example I will retrieve the imdb id of an episode.

.. code-block:: python

    >>> ep = tvdb.Episode(5330530)
    >>> response = ep.info()
    >>> ep.imdbId
    'tt4701544'

We can of course search for a tv show.. In this example I will search for doctor who series.

.. code-block:: python

    >>> search = tvdb.Search()
    >>> reponse = search.tvseries("doctor who 2005")
    >>> search[0]['seriesName']
    'Doctor Who (2005)'
