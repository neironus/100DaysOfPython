"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request

# prep

tempfile = os.path.join('/tmp', 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


def gen_files():
    """return a generator of dir names reading in `tempfile`

       `tempfile` has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile) as f:
        for line in f.readlines():
            path, is_dir = line.split(',')
            folder, user = path.split('/')

            if is_dir.strip() == 'True' and user not in IGNORE:
                yield (folder, user)


def diehard_pybites():
    """return a Stats namedtuple (defined above) that has the user that
       most PR'd and a tuple of most popular challenge = (challenge, num_prs)
       see the test for the exected values"""

    for folder, user in gen_files():
        users[user] += 1
        popular_challenges[folder] += 1

    return Stats(
        users.most_common(1)[0][0], popular_challenges.most_common(1)[0]
    )


if __name__ == '__main__':
    t = diehard_pybites()
    print(t)
