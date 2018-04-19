#!/usr/bin/env python
import os
import vlc
from collections import namedtuple

Sound = namedtuple('Sound', 'title path')


# Init the list of sounds
def init_list_sounds():
    sounds = []
    files = os.listdir('./mp3')

    # Extract the title of the name. The - are replaced by space
    for file in files:
        firstPart = file.split('.')[0]  # Split by . removing the extension
        title = " ".join(firstPart.split('-'))
        sounds.append(Sound(title, file))

    return sounds


# Print the list
def list_sounds():
    for i, sound in enumerate(sounds):
        print("%d - %s" % (i, sound['title']))


sounds = init_list_sounds()
p = vlc.MediaPlayer('')

quit = False
while(quit is not True):
    q = raw_input('Enter !q for quit or !l for list sound.\n').lower()

    if q == '!q':
        quit = True
    elif q == '!l':
        list_sounds()
    else:
        try:
            q = int(q)
            if 0 <= q < len(sounds):
                p.stop()
                p = vlc.MediaPlayer('./mp3/' + sounds[q].path)
                p.play()
        except Exception as e:
            print(e)

    print('\n\n')

print('QUITT')
