import uplink
import requests

from uplink_helpers import raise_for_status


@raise_for_status
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('api/search/{keyword}')
    def search_movie(self, keyword):
        """Search by keyword"""

    @uplink.get('api/director/{director}')
    def search_director(self, director):
        """Search by director"""

    @uplink.get('api/movie/{imdb_number}')
    def search_imdb_number(self, imdb_number):
        """Get a movie by his imdb_number"""
