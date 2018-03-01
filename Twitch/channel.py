import config as cfg
from db import DB
import urllib2, json
import threading

d = DB()

class Channel:
    def __init__(self, username):
        self.username = username

    def start(self):
        self._timer = threading.Timer(10, self._run)
        self._timer.start()

    def stop(self):
        self._timer.cancel()

    def _run(self):
        self._status()
        self.start()

    def _status(self):
        url = 'https://api.twitch.tv/kraken/streams/' + self.username
        req = urllib2.Request(url)
        req.add_header("Client-ID",cfg.twitch['client_id'])
        resp = urllib2.urlopen(req)
        content = json.loads(resp.read())

        if content.get('stream') and content.get('stream').get('viewers'):
            print "%s - %d" % (self.username, content.get('stream').get('viewers'))
            d.insert('viewers', {'user': self.username, 'viewers': content.get('stream').get('viewers')})
        else:
            print "%s - Offline" % (self.username)
