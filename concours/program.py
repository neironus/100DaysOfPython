import logbook
import config as cfg
from actors.twitter import Twitter
from actors.db import DB


def init_logging():
    level = logbook.TRACE

    logbook.TimedRotatingFileHandler(
        'logs/logs.log', level=level
    ).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        'file mode: logs.log'
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


def main():
    db = DB(cfg.mongodb.get('host'), cfg.mongodb.get('db'))

    t = Twitter(
        cfg.twitter.get('consumer_key'), cfg.twitter.get('consumer_secret'),
        cfg.twitter.get('access_token'),
        cfg.twitter.get('access_token_secret'), db
    )
    t.search_hashtags('concours')


if __name__ == '__main__':
    init_logging()
    main()