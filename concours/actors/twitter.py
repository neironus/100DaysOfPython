# https://python-twitter.readthedocs.io/en/latest/twitter.html
import twitter
import logbook
from pprint import pprint

twitter_log = logbook.Logger('Twitter')


class Twitter(object):
    def __init__(self, key, secret, token, token_secret):
        self.api = twitter.Api(
            consumer_key=key,
            consumer_secret=secret,
            access_token_key=token,
            access_token_secret=token_secret,
            sleep_on_rate_limit=True
        )

    # Generate the post url
    def generate_url_tweet(self, username, id):
        print('https://twitter.com/{}/status/{}'.format(username, id))

    # Make a query with the term keyword
    def get_posts(self, keyword):
        results = self.api.GetSearch(term=keyword)

        twitter_log.info(
            'Search {} - {} results'.format(keyword, len(results))
        )

        self.exploit_results(results)

    # Search for a specific hashtag
    def search_hashtags(self, hashtags):
        self.get_posts('#{}'.format(hashtags))

    # Exploit list of results
    def exploit_results(self, results):
        print('> {} results'.format(len(results)))

        for result in results:
            self.exploit_post(result)

    # Exploit a post
    def exploit_post(self, post):
        if post.text[0:2] != 'RT':
            self.generate_url_tweet(post.user.screen_name, post.id_str)
            # self.follow_users(post.user_mentions)
            # self.follow_users(post.user)
            # self.retweet(post)
            # print(post)
            print('\n\n\n')

    # Follow several users
    def follow_users(self, user_mentions):
        for user in user_mentions:
            self.follow_user(user)

    # Follow a user
    def follow_user(self, user):
        if not self.is_friend_with(user.id):
            twitter_log.info(
                'Follow user {} with id {}'.format(user.screen_name, user.id)
            )
            self.api.CreateFriendship(user.id)

    # Retweet a post
    def retweet(self, post):
        twitter_log.info('Retweet post {}'.format(post.id))
        self.api.PostRetweet(post.id)

    # Check if you follow the user
    def is_friend_with(self, id):
        users = self.api.LookupFriendship(user_id=id, return_json=True)

        if len(users) > 0:
            return False if 'none' in users[0].get('connections') else True
        return False
