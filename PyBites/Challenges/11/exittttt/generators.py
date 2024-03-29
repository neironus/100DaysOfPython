import glob, random
"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""

def gen_files(pat):
    yield from glob.glob(pat)

def gen_lines(files):
    for file in files:
        with open(file, 'r') as fileo:
            for row in fileo:
                yield row

def gen_grep(lines, pattern):

def gen_count(lines):
    pass


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../../*/*.py')
    lines = gen_lines(files)

