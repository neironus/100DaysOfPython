import requests
import json
from collections import namedtuple
from typing import List

Movie = namedtuple('Movie', 'imdb_code, title, director, keywords, duration,'
                            'genres, rating, year, imdb_score')


class EmptyTitleException(Exception):
    pass


def search_by_title(title: str) -> List[Movie]:
    url = 'http://movie_service.talkpython.fm/api/search/'

    if not title.strip():
        raise EmptyTitleException('Title can\'t be empty.')

    try:
        res = requests.get(url+title)
        res.raise_for_status()

        results = json.loads(res.text)

        return sorted(
            [Movie(**row) for row in results.get('hits')],
            key=lambda m: -m.year
        )
    except Exception as e:
        raise e from e
