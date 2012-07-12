#! /usr/bin/env python

def myDecorator(func):
    print func.__name__, 'in my Decorator'
    def new_func():
        '''new_func doc
        '''
        print 'entering', func.__name__
        func()
        print 'exited', func.__name__
        print ''
    return new_func

@myDecorator
def func1():
    ''' func1 doc string'''
    print "in func1"

@myDecorator
def func2():
    print "in func2"

  

from functools import wraps
def newDecorator(func):
    print func.__name__, 'in new decorator'
    @wraps(func)
    def new_func():
        '''New func in new decorator'''
        print 'entering', func.__name__
        func()
        print 'exited', func.__name__
        print ''
    return new_func

@newDecorator
def func3():
    '''func3 doc string'''
    print "in func3"

    
func1()
func2()
print func1.__name__
print func1.__doc__
    
func3()
print func3.__name__
print func3.__doc__
 