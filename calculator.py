"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if a == 0: raise ValueError("Cannot divide by 0")
        return b / a
    except ValueError as e:
        print(str(e))

def logarithm(a, b):
    try:
        if a == 0: raise ValueError("Can only take the logarithm of a positive number")
        elif b == 0: raise ValueError("Can only take a logarithm with base of a positive number")
        return math.log(a, b)
    except ValueError as e:
        print(str(e))
        return 0

def exponent(a, b):
    return a ** b
