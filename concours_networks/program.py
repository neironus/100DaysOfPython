from actors.twitter import Twitter
import config as cfg
import json
import logbook

app_log = logbook.Logger('APP')


def init_logging():
    level = logbook.TRACE

    logbook.TimedRotatingFileHandler(
        'logs/logs.log', level=level
    ).push_application()

    msg = 'Startup - Logging initialized, level: {}, mode: {}'.format(
        level,
        'file mode: logs.log'
    )

    app_log.notice(msg)


def add_in_file(filename, text):
    with open(filename, 'w') as file:
        file.write('{}'.format(text))


def read_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    init_logging()
    t = Twitter(
        cfg.twitter.get('consumer_key'), cfg.twitter.get('consumer_secret'),
        cfg.twitter.get('access_token'),
        cfg.twitter.get('access_token_secret')
    )

    accounts = read_from_file('accounts.json')
    datas = {}
    for id, followers in accounts.items():
        # if len(followers) == 0:
            results = t.search(id)
            app_log.notice('For {} - {}'.format(id, results))
            datas[str(id)] = None if len(results) == 0 else results
            for account in results:
                datas[str(account)] = []
        # else:
        #     datas[str(id)] = followers
    else:
        add_in_file('accounts.json', json.dumps(datas))


if __name__ == '__main__':
    main()
