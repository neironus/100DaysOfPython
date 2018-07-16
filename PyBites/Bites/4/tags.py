import os
import re
from collections import Counter
import urllib.request

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()
# start coding


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    t = TAG_HTML.findall(content)
    return Counter(t).most_common(n)


if __name__ == '__main__':
    t = get_pybites_top_tags()
    print(t)
