import logbook
import sys
from actors import Game

app_log = logbook.Logger('App')


def init_logging(filename=None):
    level = logbook.TRACE

    if not filename:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
    else:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if not filename else 'file mode: ' + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


def main():
    game = Game(10, 5, 20)
    game.play()


if __name__ == '__main__':
    init_logging('logs.log')
    main()
