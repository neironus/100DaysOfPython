import api
import webbrowser


def open_link(episode):
    base_url = 'https://talkpython.fm'
    webbrowser.open('{}{}'.format(base_url, episode.url), new=2)


def main():
    keyword = input('Keyword to search: ')
    results = api.search_keyword(keyword)
    print('There is {} results'.format(len(results)))
    for idx, r in enumerate(results):
        print('{:>3} - {:10} - {}'.format(idx, r.category, r.title))

    # print('\n{:#^20}'.format(' WORDS FOUNDS '))

    if len(results) > 0:
        go_to = input('Enter a number for listen the epiode: ')
        if 0 <= int(go_to) < len(results):
            open_link(results[int(go_to)])
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
