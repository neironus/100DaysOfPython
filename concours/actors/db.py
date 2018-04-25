#!/usr/bin/env python
from pymongo import MongoClient
from datetime import datetime


class DB:
    def __init__(self, host, db):
        mc = MongoClient(host)
        self.db = mc[db]

    def insert(self, collection, datas):
        datas['created_at'] = datetime.now()
        self.db[collection].insert_one(datas)

    def find_one(self, collection, where):
        return self.db[collection].find_one(where)
