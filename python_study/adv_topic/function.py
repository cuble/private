#!/usr/bin/env python

class c:
    def fun(self):
        return 1

def fun(p1, p2, p3='1'):
    return p3

fun_self=hasattr(fun, 'im_self')
fun_code=hasattr(fun, 'func_code')
print 'fun_self:', fun_self, ' fun_code:', fun_code
print dir(fun)
print ''

c1=c()

c_fun_self=hasattr(c.fun, 'im_self')
c_fun_code=hasattr(c.fun, 'func_code')
c1_fun_self = hasattr(c1.fun, 'im_self')
c1_fun_code = hasattr(c1.fun, 'func_code')
print 'c_fun_self:', c_fun_self, 'c_fun_code:', c_fun_code
print dir(c.fun)

print ''

print 'c1_fun_self:', c1_fun_self, 'c1_fun_code:', c1_fun_code

print ''

dic={'p1':1, 'p2':2, 'p3':3}
if 'p1' in dic: print "it's in"
