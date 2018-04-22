from collections import namedtuple
import logbook

LIST_WORDS = './eff_large_wordlist.txt'

app_log = logbook.Logger('App')
Word = namedtuple('Word', 'code, word')


def init_logging():
    level = logbook.TRACE

    logbook.TimedRotatingFileHandler('logs.log', level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        'file mode: logs.log'
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


def get_list_words():
    words = []

    try:
        with open(LIST_WORDS) as f:
            for line in f.readlines():
                s = line.split()
                words.append(Word(s[0], s[1]))
    except FileNotFoundError:
        msg = '{} File not found'.format(LIST_WORDS)
        app_log.error(msg)
        print(msg)
    except IndexError:
        msg = 'File is not correct. Index out of range error.'
        app_log.error(msg)
        print(msg)
    except Exception as e:
        app_log.exception(e)
        print(e)

    return words


def list_words(words):
    for word in words:
        print_word(word)


def print_word(word):
    print('{} - {}'.format(word.code, word.word))


def find_words(words, code):
    founds = filter(lambda x: x.code.startswith(code), words)
    if founds:  # trouble here, if not words founds
        print('\n{:#^20}'.format(' WORDS FOUNDS '))
        for f in founds:
            print_word(f)
        print('{:#<20}'.format(''))
    else:
        print('\n{:#^20}'.format(' NO WORDS FOUNDS '))


def valid_choice(choice):
    return 1 <= len(choice) <= 5 and choice.isdigit()


def run_loop(words):
    quit = False
    while(quit is not True):
        choice = input('Enter !q for quit, !l for list of code/words '
                       'or numbers.\n').lower()

        if choice == '!q':
            quit = True
        elif choice == '!l':
            list_words(words)
        else:
            if valid_choice(choice):
                find_words(words, choice)
            else:
                msg = '{} - Is not a valid choice.'.format(choice)
                app_log.error(msg)
                print('\n{}'.format(msg))

        print('\n')

    print('QUITT')


def main():
    words = get_list_words()

    if words:
        run_loop(words)


if __name__ == '__main__':
    init_logging()
    main()
