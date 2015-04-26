#! /usr/bin/Python

# Import class to manage Omdb Api.
from OmdbApi import MoviesApi

# Import json parser.
import json

# Import sys library.
import sys

params = len (sys.argv)

# Usage python3 ./SampleOmdbApi.py Film_title
# Usage python3 ./SampleOmdbApi.py Bakuman

if (params == 1):
    print ("We need at least one film title to start searching")
elif (params > 1):
    movies = MoviesApi()

    # It searchs into API every title we got at argument.
    for title in range (1, params) :
        # Title to search.
        print ("Searching: " + sys.argv[title])

        # First we need to do a query with the film title.
        movies.findFilmByTitle (sys.argv[title])
        # Second we get all movies returned by API.
        moviesList = movies.getResults ()

        # Print all films/series found
        for movie in moviesList:
            print (movie['Title'])
            print ("")
