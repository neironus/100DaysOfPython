import twitter
import re


class Twitter(object):
    def __init__(self, key, secret, token, token_secret):
        self.api = twitter.Api(
            consumer_key=key,
            consumer_secret=secret,
            access_token_key=token,
            access_token_secret=token_secret,
            sleep_on_rate_limit=True
        )

    def interesting_user(self, user):
        return self.does_contain_keywords(user)

    def does_contain_keywords(self, user):
        return re.search('#(.+)NoFake|legit', user.description)

    def search(self, user_id):
        followers = self.api.GetFollowers(user_id=user_id)
        return [user.id for user in followers if self.interesting_user(user)]
