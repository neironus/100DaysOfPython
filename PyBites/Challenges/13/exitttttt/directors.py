import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = '../movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960


Movie = namedtuple('Movie', 'title, year, score')
Filmography = namedtuple('Filmography', 'name, score, movies')

def get_movies_by_director():
    directors = defaultdict(list)
    with open(MOVIE_DATA) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if(int(row['title_year']) > MIN_YEAR):
                    movie = Movie(title=row['movie_title'], year=int(row['title_year']), score=float(row['imdb_score']))
                    directors[row['director_name']].append(movie)
            except ValueError:
                continue

    for did, movies in directors.items():
        directors[did] = sorted(movies, key=lambda x: x.score, reverse=True)

    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    return {(directors,_calc_mean(movies)):movies for directors, movies in directors.items() if len(movies) >= MIN_MOVIES}

def _calc_mean(movies):
    return round(sum(movie.score for movie in movies) / len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    report = sorted(directors.items(), key=lambda x: (float(x[0][1]), x[0][0]) , reverse=True)[:NUM_TOP_DIRECTORS]

    for i, (director, movies) in enumerate(report):
        print(' ')
        print(fmt_director_entry.format(counter=i+1, director=director[0], avg=director[1]))
        print(sep_line)
        for movie in movies:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))



def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    # print(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
