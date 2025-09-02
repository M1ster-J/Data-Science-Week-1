"""
Author: Mister J
Date: 2025-08-26
Project: Python Functions
Description:
    Demonstrates Python function concepts, including:
    - Defining and calling functions
    - Using return values
    - Docstrings for documentation
    - Default arguments
    - Higher-order functions (functions as arguments)
"""

# Example: function to find the smallest difference among three numbers
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers among a, b, and c."""
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# Test the function
print(least_difference(1, 1000, 100))


# Function with a docstring example
def least_differences(a, b, c):
    """
    Return the smallest difference between any two numbers among a, b, and c.

    Example:
    >>> least_differences(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_differences(1, 5, -5))


# Demonstrating default return value (None) and print
mystery = print("Print")
print("Returned value of print():", mystery)


# Using 'sep' to format print statements
print(1, 2, 3, 4, sep=' - ')


# Function with default argument
def greetings(who='collin'): 
    print("Hello,", who)

greetings()
greetings(who="Kaggle")
greetings("world")


# Function using input
def printing(name):
    print(name)

printing(input("What's your name? "))


# Higher-order functions: functions as arguments
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call a function on an argument"""
    return fn(arg)

def squared_call(fn, arg):
    """Return the square of the result of calling fn on arg"""
    return fn(fn(arg))

# Test higher-order functions
print(call(mult_by_five, 1))
print(squared_call(mult_by_five, 1))
