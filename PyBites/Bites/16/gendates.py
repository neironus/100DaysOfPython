from datetime import datetime
from datetime import timedelta

from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date = PYBITES_BORN + timedelta(days=100)
    birthday = PYBITES_BORN + timedelta(days=365)

    while True:
        if date > birthday:
            yield birthday
            birthday = birthday + timedelta(days=365)
        else:
            yield date
            date = date + timedelta(days=100)

    # Answer
    # days = 0
    # while True:
    #     days += 1
    #     if days % 100 == 0 or days % 365 == 0:
    #         yield PYBITES_BORN + timedelta(days=days)


if __name__ == '__main__':
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 100))

    print(dates[:10])
