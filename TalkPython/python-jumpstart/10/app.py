import sys

import requests.exceptions
import movie_service as ms


def print_headers():
    print('-------------------------------')
    print('        MOVIE SEARCH APP')
    print('-------------------------------')


def run_loop():
    title = ''
    while title is not 'x':
        print()
        try:
            title = input('Enter search text (x to exit): ')

            if title == 'x':
                print('> Bye')
                sys.exit()

            results = ms.search_by_title(title)

            if results:
                print('> There is {} results'.format(len(results)))
                print()
                for movie in results:
                    print('{} -- {}'.format(movie.year, movie.title))
            else:
                print('> No movies for this research.')

        except ms.EmptyTitleException:
            print('> The search can\'t be empty.')
        except requests.exceptions.ConnectionError:
            print('> There is a problem with your network.')
        except Exception as e:
            print('> Error: {}'.format(e))
            sys.exit()


def main():
    print_headers()
    run_loop()


if __name__ == '__main__':
    main()
