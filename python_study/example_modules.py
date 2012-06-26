#! /usr/bin/env python

from index import *

idx("Try run a shell comammand and get the output")
print "do it by command"
import commands 
result = commands.getoutput('date')
print "date is: ",
print result

print ""
print "do it by subprocess"
import subprocess as sub
p = sub.Popen('date', stdout=sub.PIPE, stderr=sub.PIPE)
#p.poll() will return the exit status of the command,
#and it will return None in case command is running
output, errors=p.communicate()
print "date is: "+output
print "command status is:" + errors

idx("Try datetime module")
import datetime
import time
d1=datetime.date.today()
dt1=datetime.datetime.now()
t1=dt1.time()
time.sleep(3)
dt2=datetime.datetime.now()
dd=dt2-dt1
print d1
print dt1
print dt2
print "type of dd is:",
print type(dd),
print "and dd is: ",
print dd
print "type of t1 is:",
print type(t1),
print "and t1 is:",
print t1


