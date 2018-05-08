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


def save_json(filename, variable):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(variable, indent=4, ensure_ascii=False))


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
    datas = accounts.copy()
    for id, followers in accounts.items():
        if len(followers) == 0:
            results = t.search(id)
            app_log.notice('For {} - {}'.format(id, results))

            data = None
            if len(results):
                data = [result.id for result in results]
            datas[str(id)] = data

            for account in results:
                datas[str(account.id)] = []

        save_json('accounts.json', datas)


if __name__ == '__main__':
    main()
