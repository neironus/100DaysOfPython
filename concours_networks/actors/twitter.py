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

    def query_accounts_informations(self, ids):
        batch_len = 100
        batches = (ids[i:i + batch_len] for i in range(
            0, len(ids), batch_len))
        users = []
        for idx, batch in enumerate(batches):
            print('Batch {}'.format(idx))
            print(batch)
            users_list = self.api.UsersLookup(user_id=batch)
            users += [
                user for user in users_list if self.interesting_user(user)
            ]

        return users

    def interesting_user(self, user):
        return self.does_contain_keywords(user)

    def does_contain_keywords(self, user):
        return re.search('#(.+)NoFake|legit', user.description)

    def search(self, user_id):
        followers = self.api.GetFollowerIDs(user_id=user_id)
        friends = self.api.GetFriendIDs(user_id=user_id)
        ids = list(set(followers) | set(friends))
        return self.query_accounts_informations(ids)


    def test(self):
        self.query_accounts_informations([783636174560722944, 963771131097329667])
        # datas = self.api.UsersLookup(user_id=[783636174560722944, 963771131097329667])
        # for user in datas:
        #     print(user.description)
        #     print('\n\n\n')
