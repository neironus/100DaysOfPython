import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    permutations = _get_permutations_draw(draw)
    words = ["".join(word).lower() for word in permutations]

    #https://www.programiz.com/python-programming/set
    return set(words) & set(dictionary)


def _get_permutations_draw(draw):
    for x in range(len(draw)+1):
        yield from list(itertools.permutations(draw, x))

def main():
    get_possible_dict_words('T, I, I, G, T, T, L'.split(', '))

if __name__ == '__main__':
    main()
