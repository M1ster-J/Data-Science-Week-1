"""
Author: Mister J
Date: 2025-08-26
Project: Booleans and Conditions
Description:
    Demonstrates how to use boolean logic, conditions, and basic functions in Python.
    Covers:
    - If/else statements
    - Comparison operators
    - Defining and using functions
"""

# Function that prints True or False based on input
def true_or_false(x):
    if x:
        print('This is true!')
    else: 
        print('This is false!')

# Example usage
true_or_false(False)


# Function to check if someone can vote
def can_vote(age):
    if age >= 18: 
        print('This user CAN vote!')
    else:
        print("This user CANNOT vote")

# Prompt user for age and check
can_vote(int(input("What's your age? ")))


# Function to check if a number is even
def is_even(x):
    if x % 2 == 0:
        print("This number is EVEN!")
    else:
        print("This number is ODD!")

# Prompt user for number
is_even(int(input("Enter a number to see if it's even or odd: ")))


# Function to check if a number is odd
def is_odd(x):
    return x % 2 == 1

# Examples
print("Is 120 odd? ", is_odd(120))
print("Is -1 odd? ", is_odd(-1))


# Check if a number is less than or equal to 100
number = int(input("Enter a number to see if it's less than or equal to 100: "))
if number <= 100:
    print("This number is less than or equal to 100")
else: 
    print("This number is greater than 100")


# Function that prints a message based on weather input
def todays_weather(weather):
    if weather.lower() == "sunny": 
        print("It's a nice day!")
    elif weather.lower() == "rainy":
        print("Don't forget your umbrella!")
    elif weather.lower() == "snowy":
        print("Brrr, stay warm!")
    else:
        print("Hmm, I'm not sure about that weather.")

# Prompt user for weather
todays_weather(input("What's the weather like today? (sunny, rainy, snowy): "))


# Boolean examples
print("bool(1):", bool(1))
print("bool('asf'):", bool('asf'))
print("bool(''):", bool(''))
