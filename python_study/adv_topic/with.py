#! /usr/bin/env python

class myCM:
    def __init__(self):
        self.param = 1

    def __enter__(self):
        print "entering cm"
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.param = 0
        print "exited from myCM"
        return True


with myCM() as cm:
    print "doing something with cm, cm.param=%d"%cm.param
print "cm.param=%d"%cm.param

