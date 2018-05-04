from actors.twitter import Twitter
import config as cfg
import json


def add_in_file(filename, text):
    with open(filename, 'w') as file:
        file.write('{}'.format(text))


def read_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    t = Twitter(
        cfg.twitter.get('consumer_key'), cfg.twitter.get('consumer_secret'),
        cfg.twitter.get('access_token'),
        cfg.twitter.get('access_token_secret')
    )

    accounts = read_from_file('accounts.json')
    datas = {}
    for id, followers in accounts.items():
        if len(followers) == 0:
            results = t.search(id)
            datas[str(id)] = results
            for account in results:
                datas[str(account)] = []
        else:
            datas[str(id)] = followers
    else:
        add_in_file('accounts.json', json.dumps(datas))


if __name__ == '__main__':
    main()
