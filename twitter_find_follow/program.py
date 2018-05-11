import tweepy
from collections import namedtuple
import csv
import sys

import config as cfg

User = namedtuple('User', 'id screen_name description following')
Tweet = namedtuple('Tweet', 'id text user')

auth = tweepy.OAuthHandler(
    cfg.twitter.get('consumer_key'),
    cfg.twitter.get('consumer_secret')
)
auth.set_access_token(
    cfg.twitter.get('access_token'),
    cfg.twitter.get('access_token_secret')
)

api = tweepy.API(auth)

new_follows = []


def save_follows():
    with open('follows.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(new_follows)


class FindInterestingUser(object):

    def findByKeyword(self, keyword):
        tweets = api.search(
            q=keyword, count=100, result_type='recent', tweet_mode='extended'
        )
        return self.reformat_tweet(tweets)

    def reformat_tweet(self, tweets):
        for t in tweets:
            u = User(
                t.author.id, t.author.screen_name, t.author.description,
                t.author.following
            )
            yield Tweet(t.id_str, t.full_text, u)

    def print_tweet(self, tweet):
        print('\n\n##########################################')
        print('{} \nby {} - {}'.format(
            tweet.text, tweet.user.screen_name, tweet.user.description
        ))
        print('##########################################\n')
        self.ask_for_follow(tweet.user)

    def ask_for_follow(self, user):

        if user.following:
            return

        msg = 'Do you want to follow this user ? [y]es or [n]o '
        qa = input(msg)

        if qa == 'y':
            self.follow_user(user)

    def follow_user(self, user):
        api.create_friendship(user_id=user.id)
        new_follows.append([user.id, user.screen_name])


def main():
    if len(sys.argv) != 2:
        print('Need a keyword/hashtags')


    f = FindInterestingUser()
    tweets = f.findByKeyword(sys.argv[1])
    for t in tweets:
        f.print_tweet(t)
    save_follows()


if __name__ == '__main__':
    main()
