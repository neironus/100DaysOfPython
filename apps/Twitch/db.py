#!/usr/bin/env python
from pymongo import MongoClient
import config as cfg
from datetime import datetime

urlMongoDB = cfg.mongodb['host']

class DB:
    def __init__(self):
        mc = MongoClient(urlMongoDB)
        self.db = mc.twitch

    def insert(self, collection, datas):
        datas['created_at'] = datetime.now()
        self.db[collection].insert_one(datas)
