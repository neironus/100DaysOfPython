import logbook
import config as cfg
from actors.twitter import Twitter
from actors.db import DB

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


def main():
    db = DB(cfg.mongodb.get('host'), cfg.mongodb.get('db'))

    t = Twitter(
        cfg.twitter.get('consumer_key'), cfg.twitter.get('consumer_secret'),
        cfg.twitter.get('access_token'),
        cfg.twitter.get('access_token_secret'), db
    )

    if cfg.debug:
        t.search_hashtags(['freebiefriday'])
    else:
        t.search_hashtags([
            'concours', 'jeuconcours', 'giveaway', 'gagner', 'jeu', 'win',
            'prize', 'freebiefriday', 'fridayfreebie', 'competition'
        ])

    app_log.notice('Quit App')


if __name__ == '__main__':
    init_logging()
    main()
