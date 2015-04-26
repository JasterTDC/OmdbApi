#! /usr/bin/Python

# Import library to work with urls.
import urllib
from urllib.request import urlopen

# Import json library to parse json files.
import json

class MoviesApi :
    # Class constructor.
    def __init__ (self):
        self.urlApi = "http://www.omdbapi.com"
        self.results = []
        self.numItems = 0

    # Find a film using a title as a parameter
    def findFilmByTitle (self, title):
        self.title = title

        # Read the content of the url.
        searchUrl = self.urlApi + "/?s=" + self.title

        content = urlopen (searchUrl)
        jsonData = content.readall().decode('utf-8')
        content.close()

        # Parse the string as json.
        self.results = json.loads (jsonData)

        if "Response" in self.results :
            self.numItems = 0
        else:
            self.numItems = len (self.results["Search"])

    def findFilmById (self, imdbId):
        # Imdb identifier.
        self.imdbId = imdbId

        # Build the url.
        searchUrl = self.urlApi + "/?i=" + self.imdbId + "&plot=full&r=json"

        # Open url as a file.
        content = urlopen (searchUrl)
        jsonData = content.readall().decode('utf-8')
        content.close()

        # Parse the string as json
        self.ids = json.loads (jsonData)

    # Get results of a query.
    def getResults (self):
        if "Response" in self.results :
            return -1
        else:
            return self.results["Search"]

    # Get the entries number of query.
    def getNumItems (self):
        return self.numItems

    # Get all the information about one film.
    def getFilm (self):
        return self.ids
