"""
Author: Mister J
Date: 2025-08-26
Project: Strings and Dictionaries in Python
Description:
    Demonstrates Python string and dictionary operations:
    - String indexing, slicing, and length
    - String methods (upper, lower, startswith, endswith)
    - String formatting with format() and f-strings
    - Special characters and multi-line strings
    - Splitting and joining strings
    - Dictionary creation and manipulation
    - Dictionary comprehension
"""

# Strings
greetings = "Hello, Python!"
print(greetings)

# Special characters in strings
pluto = "pluto's a planet"
print(pluto)

what = 'what\"s up?'
print(what)

mountain = 'Look, it\'s a mountain! /\\'
print(mountain)

nline = 'This is a new line\nSee?'
print(nline)

triplequote = """This is a triple quoted string
See? It can span multiple lines,
like this!
or this! 
or this and this!"""
print(triplequote)

# String indexing
print("First character:", greetings[0])
print("Last character:", greetings[-1])
print("Length of greetings:", len(greetings))

# List comprehension with strings
chars = [char + '! ' for char in mountain]
print(chars)

# String methods
print("Uppercase greetings:", greetings.upper())
print("Lowercase mountain:", mountain.lower())
print("Index of 'h':", greetings.lower().index('h'))
print("Starts with 'Hello'? :", greetings.startswith('Hello'))
print("Ends with 'g'? :", greetings.endswith('g'))

# Splitting and joining
datestr = '05-12-2021'
year, month, day = datestr.split('-')
print("Year:", year, "Month:", month, "Day:", day)
print("Joined date:", '/'.join([month, day, year]))

# String concatenation and formatting
greet = greetings + '\n' + 'Whoever is reading this'
print(greet)

position = 3
big_mount = mountain + " Look " + str(position) + " It's a planet"
print(big_mount)

testing = '{} this is the {}rd test'.format(mountain, position)
print(testing)

# Using numbers in formatted strings
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

print("{} weighs about {:.2e} kilograms ({:.3%} of Earth's mass). It is home to {:,} plutonians.".format(
    pluto, pluto_mass, pluto_mass / earth_mass, population
))

s = """Pluto's a {0} 
no, it's a {1}. 
{0}! 
{1}!""".format('pluto', 'dwarf planet')
print(s)

# Dictionaries
numbers = {'one': 1, 'two': 2, 'three': 3}
print(numbers)
print("Value for 'two':", numbers['two'])

# Add a new key-value pair
numbers['eleven'] = 11
print("Value for 'eleven':", numbers['eleven'])

# Dictionary comprehension
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_to_initial = {planet: planet[0] for planet in planets}
print("Planets to initial:", planets_to_initial)

# Check membership (case-insensitive)
if 'Saturn'.lower() in (p.lower() for p in planets_to_initial):
    print("Saturn is in the dictionary")
else:
    print("Saturn is not in the dictionary")

# Iterate over dictionary
for k in numbers:
    print(f"{k} = {numbers[k]}")
