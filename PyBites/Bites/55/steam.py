from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    rss = feedparser.parse(FEED_URL)

    return [Game(item['title'], item['link']) for item in rss['entries']]


if __name__ == '__main__':
    get_games()
