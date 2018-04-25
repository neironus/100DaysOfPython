import logbook


def main():
    print('d')


def init_logging():
    lvl = logbook.TRACE

    logbook.TimedRotatingFileHandler('logs.log', level=lvl).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        lvl,
        'file mode: logs.log'
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging()
    main()
