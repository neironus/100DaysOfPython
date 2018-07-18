import glob
import json
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = '{}.json'.format(movie)
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    results = []
    for file in files:
        with open(file) as f:
            results.append(json.loads(f.read()))

    return results


def get_single_comedy(movies):
    return [
        movie.get('Title') for movie in movies if 'Comedy' in movie.get('Genre')
    ][0]


def extract_nomination(movie):
    return int(re.sub(r'.* (\d+) nomin.*', r'\1', movie.get('Awards')))


def get_movie_most_nominations(movies):
    # Nominated
    # for 1 Oscar.Another 10 wins & 32 nominations.
    m = max(movies, key=extract_nomination)
    return m.get('Title')


def get_movie_longest_runtime(movies):
    m = max(movies, key=lambda movie: int(movie.get('Runtime').split()[0]))
    return m.get('Title')


if __name__ == '__main__':
    movies = get_movie_data()
    c = get_single_comedy(movies)
    n = get_movie_most_nominations(movies)
    r = get_movie_longest_runtime(movies)
