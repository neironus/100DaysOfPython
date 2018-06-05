import config as cfg
from actors.db import DB
import os

db = DB(cfg.mongodb.get('host'), cfg.mongodb.get('db'))
base_folder = os.path.dirname(__file__)


def main():
    seeds_replies()


def seeds_replies():

    filename = os.path.join(
        base_folder, 'seeds', 'reply.txt'
    )
    db.clear_collection('replies')

    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            db.insert('replies', {'reply': line.strip()})
        else:
            print('> Seed replies done.')


if __name__ == '__main__':
    main()
