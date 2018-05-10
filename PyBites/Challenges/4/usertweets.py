from collections import namedtuple
import csv
import tweepy
import os

import config as cfg

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

Tweet = namedtuple('Tweet', 'id_str created_at text')


class UserTweets(object):

    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        self.output_file = os.path.join(DEST_DIR, handle + '.csv')

        auth = tweepy.OAuthHandler(
            cfg.twitter.get('consumer_key'),
            cfg.twitter.get('consumer_secret'),
        )
        auth.set_access_token(
            cfg.twitter.get('access_token'),
            cfg.twitter.get('access_token_secret'),
        )

        self.api = tweepy.API(auth)
        self._tweets = list(self._get_tweets())
        self._save_tweets()

    def _get_tweets(self):
        tweets = self.api.user_timeline(
            screen_name=self.handle,
            max_id=self.max_id,
            count=NUM_TWEETS,
        )

        return (Tweet(t.id_str, t.created_at, t.text) for t in tweets)

    def _save_tweets(self):
        with open(self.output_file, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['id_str', 'created_at', 'text'])
            for data in self._tweets:
                writer.writerow(data)

    def __len__(self):
        return len(self._tweets)

    def __getitem__(self, pos):
        return self._tweets[pos]


if __name__ == "__main__":

    for handle in ('pybites', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
