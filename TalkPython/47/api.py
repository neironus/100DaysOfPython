import requests
from collections import namedtuple


Episode = namedtuple('Episode', 'category, id, url, title, description')


def search_keyword(keyword):
    url = 'http://search.talkpython.fm/api/search?q={}'.format(keyword)
    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    episodes = []
    for r in results.get('results'):
        episodes.append(Episode(**r))

    return sorted(episodes, key=lambda x: (x.id, x.category))
