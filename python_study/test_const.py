#! /usr/bin/env python
import const

const.InvalidTime=0

if const.InvalidTime == 0: print 'OK'

try: 
    const.InvalidTime=1
except const.ConstError:
    print "const works in python2.6"

