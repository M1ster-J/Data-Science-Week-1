"""
Author: Mister J
Date: 2025-08-26
Project: Loops and Lists in Python
Description:
    Demonstrates Python loops, list comprehensions, and working with lists:
    - For loops
    - While loops
    - List comprehensions
    - Conditional list comprehensions
    - Defining functions with list comprehensions
"""

# List of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# For loop: iterate through planets
print("All planets:")
for planet in planets: 
    print(planet)

# For loop with range
print("\nNumbers 0-5:")
for i in range(6): 
    print(i)

# While loop
print("\nWhile loop 0-5:", end=' ')
i = 0
while i < 6:
    print(i, end=' ')
    i += 1
print()  # newline

# List comprehension: squares of 0-9
squares = [n**2 for n in range(10)]
print("\nSquares using list comprehension:", squares)

# Appending squares to a list using a for loop
appending = []
print("\nSquares using append in loop:")
for i in range(10):
    appending.append(i**2)
    print(appending)

# List comprehension with condition
short_planets = [planet for planet in planets if len(planet) < 10]
print("\nPlanets with names shorter than 10 characters:", short_planets)

# Uppercase + exclamation for planets with names shorter than 6 characters
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print("Loud short planets:", loud_short_planets)

# Function to count negative numbers using list comprehension
def count_negatives(nums):
    return len([n for n in nums if n < 0])

print("\nCount of negative numbers:", count_negatives([-1, 2, -3, 4, -5]))
