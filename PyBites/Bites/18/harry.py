import os
import re
import urllib.request
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_stopwords():
    with open(stopwords_file) as file:
        return [line.strip('\n').lower() for line in file.readlines()]


def get_harry_most_common_word():
    stopwords = get_stopwords()
    cnt = Counter()

    with open(harry_text) as ht:
        for l in ht.readlines():
            words = l.split()
            for word in words:
                word = re.sub(r'\W', '', word).lower()
                if word.strip() and word.lower() not in stopwords:
                    cnt[word] += 1

        return cnt.most_common(1)[0]


if __name__ == '__main__':
    print(get_harry_most_common_word())
