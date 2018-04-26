#!/usr/bin/env python
from pymongo import MongoClient
from datetime import datetime
from random import randint
import logbook

db_log = logbook.Logger('DB')


class DB:
    def __init__(self, host, db):
        mc = MongoClient(host)
        self.db = mc[db]

    def insert(self, collection, datas):
        datas['created_at'] = datetime.now()
        self.db[collection].insert_one(datas)

    def find_one(self, collection, where):
        return self.db[collection].find_one(where)

    def clear_collection(self, collection):
        return self.db[collection].drop()

    def get_random_row(self, collection):
        n = self.db[collection].count()
        if n == 0:
            msg = 'There is not replies. Seed the collection.'
            db_log.error(msg)
            raise ValueError(msg)

        return self.db[collection].find().limit(-1).skip(randint(1, n)).next()
