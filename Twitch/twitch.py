#!/usr/bin/env python
import config as cfg
import urllib2, json

channels = ['woowakgood', 'lexveldhuis', 'p4wnyhof']

for c in channels:
    url = 'https://api.twitch.tv/kraken/streams/' + c
    req = urllib2.Request(url)
    req.add_header("Client-ID",cfg.twitch['client_id'])
    resp = urllib2.urlopen(req)
    content = json.loads(resp.read())

    if content.get('stream') and content.get('stream').get('viewers'):
        print "%s - %d" % (c, content.get('stream').get('viewers'))
