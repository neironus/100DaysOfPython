from api import MovieSearchClient


def ask_for_searchword():
    return input('Search for: ')


def prints_results(results):
    if results:
        for result in results:
            print('{} by {} rate {}'.format(
                result.get('title'), result.get('director'),
                result.get('imdb_score')
            ))
    else:
        print('No results founds.')


def main():
    m = MovieSearchClient()

    search_by = input((
        "What do you want to search by ? [k]eyword /"
        "[d]irector / [i]mdb number. "
    ))

    if search_by == 'k':
        search = ask_for_searchword()
        resp = m.search_movie(search)
        prints_results(resp.json().get('hits'))
    elif search_by == 'd':
        search = ask_for_searchword()
        resp = m.search_director(search)
        prints_results(resp.json().get('hits'))
    elif search_by == 'i':
        search = ask_for_searchword()
        resp = m.search_imdb_number(search)
        result = resp.json()
        if result:
            print('{} by {} rate {}'.format(
                result.get('title'), result.get('director'),
                result.get('imdb_score')
            ))
        else:
            print('No results founds')
    else:
        print('Invalid option')


if __name__ == '__main__':
    main()
