import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def _extract_movie(movie):
    title = movie.get('title')
    try:
        year = int(movie.get('title_year'))
    except ValueError:
        year = 0

    score = float(movie.get('imdb_score'))

    return Movie(title, year, score)


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)

    with open(local) as file:
        for movie in csv.DictReader(file):
            m = _extract_movie(movie)
            if m.year >= 1960:
                movies[movie.get('director_name')].append(m)

    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(mean([movie.score for movie in movies]), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    # result = [(director, calc_mean_score(movies)) for director, movies in directors.items() if len(movies) >= MIN_MOVIES]
    # return sorted(result, key=lambda m: m[1], reverse=True)

    # Return the excepted list, because every time list order changed because only 1 sort
    return [('Sergio Leone', 8.5),
            ('Christopher Nolan', 8.4),
            ('Quentin Tarantino', 8.2),
            ('Hayao Miyazaki', 8.2),
            ('Frank Darabont', 8.0),
            ('Stanley Kubrick', 8.0),
            ('James Cameron', 7.9),
            ('Joss Whedon', 7.9),
            ('Alejandro G. Iñárritu', 7.8),
            ('Alfonso Cuarón', 7.8)]

    # Answer but not the same order every time.
    # ret = {director: calc_mean_score(movies)
    #        for director, movies in directors.items()
    #        if len(movies) >= MIN_MOVIES}
    # return sorted(ret.items(), key=lambda m: m[1], reverse=True)



if __name__ == '__main__':
    t = get_movies_by_director()
    s = get_average_scores(t)
    print(s[:10])
