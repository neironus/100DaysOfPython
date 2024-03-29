import os
import re
from difflib import SequenceMatcher
from itertools import product
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve('http://bit.ly/2zD8d8b', TEMPFILE)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()

    for pair in product(tags, tags):

        if pair[0][0] != pair[1][0]:
            continue

        seq = SequenceMatcher(None, *pair)
        if SIMILAR <= seq.ratio() < IDENTICAL:
            yield pair


if __name__ == '__main__':
    for x in get_similarities():
        print(x)
