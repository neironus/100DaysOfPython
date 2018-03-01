#!/usr/bin/env python
import stats

stats.startAll()

quit = False
while(quit != True):
    q = raw_input('Enter !q for quit.\n').lower()
    if(q == '!q'):
        quit = True
    else:
        print(quit)

stats.stopAll()
