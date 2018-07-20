import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/dates/'
RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


dates = _get_dates()


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    # 'Tue, 27 Dec 2016 00:10:00 +0100'
    return datetime.strptime(date_str[:-6], '%a, %d %b %Y %X')


def extract_day_month(date):
    return '{}-{:02d}'.format(date.year, date.month)


def get_month_most_posts(dates):
    """Receives a list of date strings and returns the month (format YYYY-MM)
       that occurs most"""
    dates = [extract_day_month(date) for date in dates]
    c = collections.Counter(dates)
    return c.most_common(1)[0][0]

