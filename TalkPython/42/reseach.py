import os
import csv
from collections import namedtuple
data = []


Record = namedtuple('Record', '')


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(
        base_folder, 'data', 'thanksgiving-2015-poll-data.csv'
    )

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = Record(**row)
            print(record)
