# https://github.com/gavin-hensley63/lab11-GH-ZM
# Partner 1: Gavin Hensley
# Partner 2: Zijian Mao


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
# First example

def add(a, b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    if a==0:
        raise ZeroDivisionError
    return b/a
def exp(a,b):
    return a**b


def square_root(a):
    if a < 0: raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a == 0: raise ValueError("Can only take the logarithm of a positive number")
    if b == 0: raise ValueError("Can only take a logarithm with base of a positive number")
    if a == 1: raise ValueError("Cannot take the logarithm of 1")
    if b == 1: raise ValueError("Cannot take the logarithm with base of 1")
    return math.log(a, b)
