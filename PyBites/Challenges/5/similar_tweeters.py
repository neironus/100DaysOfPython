import sys
import tweepy
from gensim import corpora
import re
from collections import Counter

import config as cfg

auth = tweepy.OAuthHandler(
    cfg.twitter.get('consumer_key'),
    cfg.twitter.get('consumer_secret'),
)
auth.set_access_token(
    cfg.twitter.get('access_token'),
    cfg.twitter.get('access_token_secret'),
)
api = tweepy.API(auth)


def get_last_tweets(screen_name):
    timeline = api.user_timeline(screen_name=screen_name, count=200)
    tweets = [t.text for t in timeline]
    tweets = clean_tweets(tweets)

    flatten = [word for words in tweets for word in words]
    return remove_single_occurence(flatten)


def clean_tweets(tweets):
    return [
        [word for word in tweet.lower().split() if clean_word(word)]
        for tweet in tweets
    ]


def clean_word(word):
    stoplist = ''.split()

    longer = len(word) > 3
    in_stoplist = word not in stoplist
    not_link = not word.startswith('http')
    no_tag_hashtag = not re.match(r'@|#', word)

    return longer and in_stoplist and not_link and no_tag_hashtag


def remove_single_occurence(words):
    counter = Counter(words)
    return [word for word in words if counter[word] > 1]


def similar_tweeters(user1, user2):
    user1_tweet = get_last_tweets(user1)
    user2_tweet = get_last_tweets(user2)

    dictionary = corpora.Dictionary([user1_tweet, user2_tweet])
    print(dictionary.token2id)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
