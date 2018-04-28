# https://python-twitter.readthedocs.io/en/latest/twitter.html
import twitter
import logbook
import urllib
from pprint import pprint
from time import sleep
from random import randint, sample
import config as cfg

MAX_COUNT = 100
FILTERED_MIN = 2

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
        print('> https://twitter.com/{}/status/{}'.format(username, id))

    # Make a query with the term keyword
    def get_posts(self, keyword):
        self._sleep_random()
        query = urllib.parse.urlencode({
            'q': keyword, 'count': MAX_COUNT, 'result_type': 'recent',
            'tweet_mode': 'extended'
        })
        results = self.api.GetSearch(raw_query=query)

        twitter_log.trace(
            'Search {} - {} results'.format(keyword, len(results))
        )

        self.exploit_results(results)

    # Search for a specific hashtag
    def search_hashtags(self, hashtags):
        for hashtag in hashtags:
            self.get_posts('#{}'.format(hashtag))

    # Exploit list of results
    def exploit_results(self, results):
        print('> {} results'.format(len(results)))

        for result in results:
            self._sleep_random(1, 9)
            self.exploit_post(result)

    # Exploit a post
    def exploit_post(self, post):
        if post.retweeted_status:
            post = post.retweeted_status

        if self.post_is_valid(post):
            # follow user mentioned in the post
            self.follow_users(post.user_mentions)

            self.follow_user(post.user)
            self.like_post(post)
            self.retweet(post)
            self.reply_post(post)
            # print('\n\n\n')
        else:
            self._insert_possible_false_negative(post)

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
            self.api.CreateFriendship(user.id)

    # Retweet a post
    def retweet(self, post):
        # Check in DB if already retweet
        post_db = self.db.find_one('retweet', {'post_id': post.id})
        if(post_db):
            return

        try:
            self.api.PostRetweet(post.id)
            self._insert_retweet_in_db(post)
            twitter_log.trace('Retweet post {} from user {} with id {}'.format(
                post.id, post.user.screen_name, post.user.id
            ))
            print('## Post retweet ##')
            self.generate_url_tweet(post.user.screen_name, post.id_str)
            print('\n\n')
        except Exception as e:
            try:
                code = e.message[0].get('code')  # Already retweet
                if code == 327:
                    self._insert_retweet_in_db(post)
            except Exception as e:
                twitter_log.exception(e)

    # Does need to like
    def does_post_need_like(self, text):
        keywords = ['like', 'aime']
        return len(self._filter_keywords(keywords, text)) > 0

    # List post
    def like_post(self, post):
        post_db = self.db.find_one('likes', {'post_id': post.id})
        if(post_db):
            return

        if self.does_post_need_like(post.full_text) or randint(0, 100) >= 90:
            try:
                self.api.CreateFavorite(status_id=post.id)
                self._insert_like_in_db(post)
            except Exception as e:
                try:
                    code = e.message[0].get('code')
                    if code == 139:  # Already like
                        self._insert_retweet_in_db(post)
                except Exception as e:
                    raise e
                twitter_log.exception(e)

    # Does need to tag friends?
    def does_i_need_tag_friend(self, text):
        keywords = ['tag a friend', 'tag']

        return len(self._filter_keywords(keywords, text)) > 0

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

    # Does the post some keywords or not
    def does_post_contain_concours_keyword(self, text):
        keywords = [' rt ', ' follow ']

        if len(self._filter_keywords(keywords, text)) >= FILTERED_MIN:
            return True
        else:
            return False

    # Post a tweet, if answer_post_id specified will answer to this post
    def post_tweet(self, status, post_owner=None, answer_post_id=None):
        if post_owner:
            status = '@{} {}'.format(post_owner, status)

        self.api.PostUpdate(
            status=status, in_reply_to_status_id=answer_post_id
        )

    # Check is the post is valid
    def post_is_valid(self, post):
        have_keyword = self.does_post_contain_concours_keyword(post.full_text)
        not_start_by_rt = post.full_text[0:2] != 'RT'
        retweet_minimum = (
            post.retweet_count >= cfg.twitter.get('minimum_retweet', 50)
        )

        return have_keyword and not_start_by_rt and retweet_minimum

    def get_friends(self, nb=1):
        friends = cfg.twitter.get('friends')
        try:
            return sample(friends, nb)
        except ValueError as e:
            twitter_log.exception(e)

    # Reply to post
    def reply_post(self, post):
        if self.does_i_need_tag_friend(post.full_text):
            friends = self.get_friends()
            if friends:
                self.post_tweet(
                    '{} :)'.format(" ".join(friends)), post.user.screen_name,
                    post.id
                )
        else:
            if self._does_i_reply():
                reply = self.db.get_random_row('replies')
                self.post_tweet(
                    reply.get('reply'), post.user.screen_name, post.id
                )

    # Insert the follow in db
    def _insert_follow_in_db(self, user):
        self.db.insert(
            'follow', {'user_id': user.id, 'username': user.screen_name}
        )

    # Insert the retweet in db
    def _insert_retweet_in_db(self, post):
        self.db.insert(
            'retweet', {
                'post_id': post.id, 'user_id': post.user.id,
                'user_name': post.user.screen_name
            }
        )

    # Insert like in db
    def _insert_like_in_db(self, post):
        self.db.insert(
            'likes', {
                'post_id': post.id, 'user_id': post.user.id,
                'user_name': post.user.screen_name
            }
        )

    # Insert the possible false negative in db
    def _insert_possible_false_negative(self, post):
        self.db.insert(
            'false_negative', {
                'post_id': post.id, 'user_id': post.user.id,
                'user_name': post.user.screen_name, "text": post.full_text
            }
        )

    # Sleep for x random seconds
    def _sleep_random(self, a=20, b=120):
        if not cfg.debug and cfg.twitter.get('sleep', 'True'):
            r = randint(a, b)
            print('sleep for {} seconds'.format(r))
            sleep(r)
            print('done sleep')

    # Check if I need to reply
    def _does_i_reply(self):
        valid_reply = ['never', 'sometime', 'always']

        try:
            reply = cfg.twitter.get('reply', 'never')
            if reply in valid_reply:
                if reply == 'never':
                    return False
                if reply == 'sometime':
                    return randint(1, 10) > 9
                if reply == 'always':
                    return True
            else:
                raise ValueError(
                    'The field reply specified in config.py is invalid'
                )
        except ValueError as e:
            twitter_log.error('{} - Current value: {}'.format(
                e, cfg.twitter.get('reply', 'empty')
            ))
            print(e)
            exit()
        except Exception as e:
            twitter_log.exception(e)
            print(e)
            raise e


    def _filter_keywords(self, keywords, text):
        return list(filter(
            lambda x: text.lower().find(x) != -1, keywords
        ))
