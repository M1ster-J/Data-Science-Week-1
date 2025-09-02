"""
Author: Mister J
Date: 2025-08-26
Project: Lists and Tuples in Python
Description:
    Demonstrates Python list and tuple operations, including:
    - Indexing
    - Membership checks
    - Length, sorting, sum, max
    - Appending and popping elements
    - Tuples vs lists
"""

# List of prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print("First prime number:", primes[0])

# Function to check if a website is in a predefined list
def websites_to_visit(site):
    websites = ['Google', 'Facebook', 'Instagram', 'Apple', 'Intel', 'AMD']
    
    if site in websites:
        print(f"Yes, {site} is in the list")
    
    # Example of modifying list element
    if 'Google' in websites:
        websites[0] = 'Not Google'
        print("Updated websites:", websites)
    else:
        print("Website not found... Try again.")
        print("First three websites:", websites[0:3])

websites_to_visit(input("Enter a website to see if it's in the list: "))


# List operations
websites = ['google', 'facebook', 'amazon', 'youtube']

print("Number of websites:", len(websites))
print("Websites sorted alphabetically:", sorted(websites))

# Operations on primes
print("Sum of primes:", sum(primes))
print("Max prime:", max(primes))

# Working with objects
x = 12
print("Imaginary part of x:", x.imag)

c = 12 + 3j
print("Imaginary part of complex number c:", c.imag)

# Append and pop
websites.append('Bing')
print("Websites after append:", websites)
websites.append('TEST')
print("Websites after second append:", websites)
websites.pop()
print("Websites after pop:", websites)

# Membership check
if 'google' in websites:
    print("Yes, it's in the list")
else:
    print("No, it's not in the list")

# Tuples
t = (1, 2, 3)
e = 1, 2, 3
sum_example = t[0] + e[1]
print("Sum of tuple elements:", sum_example)
