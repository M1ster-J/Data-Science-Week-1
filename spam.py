"""
Author: Mister J
Date: 2025-08-26
Project: Variables, Strings, and Conditionals
Description:
    Demonstrates basic Python concepts:
    - Variables and arithmetic operations
    - Conditionals (if statements)
    - String multiplication
    - String concatenation
    - Type checking and conversion
"""

# Initialize spam amount
spam_amount = 0
print("Initial spam amount:", spam_amount)

# Add 4 to spam_amount
spam_amount += 4
print("Updated spam amount:", spam_amount)

# Conditional check
if spam_amount > 0:
    print("I don't want any spam!")

# Multiply string by integer
viking_song = "Spam " * spam_amount
print("Viking song:", viking_song)

# Type checking and conversion
print("spam_amount as integer:", int(spam_amount))
print("Type of spam_amount:", type(spam_amount))
print("Type of 19.04:", type(19.04))

# String concatenation
first_name = "John"
last_name = "Doe"
age = 35
height = 6.1
weight = 180.5

print(first_name + " " + last_name)
print(f"Age: {age}, Height: {height}, Weight: {weight}")

# Storing full name in a variable
name = first_name + " " + last_name
print("Full name:", name)
