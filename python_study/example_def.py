#! /usr/bin/env python

index=0

def idx(info):
  '''Index the description of the examples'''
  print
  global index  #access to global variable
  index = index + 1
  print str(index)+". " +info #transfer int to str

def fib_core(n):
  res=[]
  a,b=0,1
  while a < n:
    res.append(a)
    a,b = b,a+b
  return res

def fib(n):
  '''Print a Fibonacci series up to n.'''
  idx("function and while loop test")
  print "fib(" + str(n) +"):",
  print fib_core(n)

def param_unpack():
  '''To test param unpack in calling function'''
  idx("Try unpack param")
  print "rang(3,6) is "+str(range(3,6))
  argsl=[3,6]
  print "argsl is "+str(argsl)
  print "And range(*argsl) is "+str(range(*argsl))
  argsd={"n":100}
  print "argsd is" + str(argsd)
  print "And fib_core(**argsd) is " + str(fib_core(**argsd))



fib(10)
param_unpack()
