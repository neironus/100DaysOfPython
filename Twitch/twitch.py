#!/usr/bin/env python
import config as cfg
from db import DB
import urllib2, json
import threading

d = DB()

def run():
    stats()
    t = threading.Timer(600 ,run) #Every 5 minutes
    t.start()

def stats():
    channels = ['woowakgood', 'lexveldhuis', 'p4wnyhof']
    for c in channels:
        url = 'https://api.twitch.tv/kraken/streams/' + c
        req = urllib2.Request(url)
        req.add_header("Client-ID",cfg.twitch['client_id'])
        resp = urllib2.urlopen(req)
        content = json.loads(resp.read())

        if content.get('stream') and content.get('stream').get('viewers'):
            print "%s - %d" % (c, content.get('stream').get('viewers'))
            d.insert('viewers', {'user': c, 'viewers': content.get('stream').get('viewers')})

run()
