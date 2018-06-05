#!/usr/bin/env python
from channel import Channel

runningChannels = []
channels = ['woowakgood', 'lexveldhuis', 'p4wnyhof', 'starladder_pubg_en']

def startAll():
    for c in channels:
        c = Channel(c)
        runningChannels.append(c)
        c.start()

def stopAll():
    for rc in runningChannels:
        rc.stop()
