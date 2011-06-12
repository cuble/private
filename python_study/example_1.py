#! /usr/bin/env python


def idx(str):
  '''Index the description of the examples'''
  index=1
  print index,
  print ". " + str

def fib(n):
  '''Print a Fibonacci series up to n.'''
  idx("function and while loop test")
  a,b=0,1
  while a < n:
    print a,
    a, b = b, a+b

index=0
fib(10)

