"""
Author: Mister J
Date: 2025-08-26
Project: Using External Libraries (Math)
Description:
    Demonstrates using Python's built-in math library, including:
    - Importing the library
    - Using constants like pi
    - Using functions like log
    - Exploring the module with dir()
"""

import math as mt
from math import pi, log

# Show the type of the math module
print("Math module type:", type(mt))

# List all functions and attributes in math module
print("Available functions in math module:\n", dir(mt))

# Display pi to 4 significant digits
print("Pi to 4 significant digits: {:.4}".format(mt.pi))

# Logarithm examples
print("Natural log of 1000:", mt.log(1000))
print("Log base 3 of 32:", log(32, 3))
print("Value of pi imported directly:", pi)
