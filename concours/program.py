import logbook
import config as cfg
from actors.twitter import Twitter


def init_logging():
    lvl = logbook.TRACE
#
    logbook.TimedRotatingFileHandler('logs/logs.log', level=lvl).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        lvl,
        'file mode: logs.log'
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


def main():
    t = Twitter(
        cfg.twitter.get('consumer_key'), cfg.twitter.get('consumer_secret'),
        cfg.twitter.get('access_token'), cfg.twitter.get('access_token_secret')
    )
    t.search_hashtags('concours')


if __name__ == '__main__':
    init_logging()
    main()
