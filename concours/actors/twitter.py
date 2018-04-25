# https://python-twitter.readthedocs.io/en/latest/twitter.html
import twitter
import logbook
from pprint import pprint

twitter_log = logbook.Logger('Twitter')


class Twitter(object):
    def __init__(self, key, secret, token, token_secret, db=None):
        self.api = twitter.Api(
            consumer_key=key,
            consumer_secret=secret,
            access_token_key=token,
            access_token_secret=token_secret,
            sleep_on_rate_limit=True
        )
        self.db = db

    # Generate the post url
    def generate_url_tweet(self, username, id):
        print('https://twitter.com/{}/status/{}'.format(username, id))

    # Make a query with the term keyword
    def get_posts(self, keyword):
        results = self.api.GetSearch(term=keyword)

        twitter_log.trace(
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
            if self.does_post_contain_concours_keyword(post.text):
                self.follow_users(post.user_mentions)
                self.follow_user(post.user)
                self.retweet(post)
                # print(post)
                print('\n\n\n')
            else:
                twitter_log.info(
                    '{} from {}, really not a concours ? {}'.format(
                        post.id_str, post.user.screen_name, post.text
                    )
                )

    # Follow several users
    def follow_users(self, user_mentions):
        if user_mentions:
            for user in user_mentions:
                self.follow_user(user)

    # Follow a user
    def follow_user(self, user):
        if not self.is_friend_with(user, insert_db=True):
            twitter_log.trace(
                'Follow user {} with id {}'.format(user.screen_name, user.id)
            )
            self._insert_follow_in_db(user)
            # self.api.CreateFriendship(user.id)

    # Retweet a post
    def retweet(self, post):
        # Check in DB if already retweet
        post_db = self.db.find_one('retweet', {'post_id': post.id})
        if(post_db):
            return

        try:
            self.api.PostRetweet(post.id)
            self._insert_retweet_in_db(post)
            twitter_log.trace('Retweet post {}'.format(post.id))
        except Exception as e:
            try:
                code = e.message[0].get('code')  # Already retweet
                if code == 327:
                    self._insert_retweet_in_db(post)
            except Exception as e:
                twitter_log.exception(e)
            pass

    # Check if you follow the user
    def is_friend_with(self, user, insert_db=False):

        # Check in DB if already follow
        user_db = self.db.find_one('follow', {'user_id': user.id})
        if(user_db):
            return True

        # Query twitter if user followed
        users = self.api.LookupFriendship(user_id=user.id, return_json=True)
        if len(users) > 0:
            if 'none' in users[0].get('connections'):
                return False
            else:
                # User already followed but the DB in not aware so insert in DB
                if insert_db:
                    self._insert_follow_in_db(user)
                return True
        return False

    def does_post_contain_concours_keyword(self, text):
        keywords = ['rt', 'follow']

        return True if list(filter(
            lambda x: text.lower().find(x) != -1, keywords
        )) else False

    # Insert the follow in db
    def _insert_follow_in_db(self, user):
        self.db.insert(
            'follow', {'user_id': user.id, 'username': user.screen_name}
        )

    def _insert_retweet_in_db(self, post):
        self.db.insert(
            'retweet', {'post_id': post.id}
        )
