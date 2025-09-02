"""
Author: Mister J
Date: 2025-08-26
Project: Working Login Form
Description:
    Demonstrates a simple login form in Python with:
    - User and password verification
    - Handling invalid usernames and passwords
    - Displaying a menu upon successful login
"""

def login(user, password_input):
    # Define valid users and passwords
    users = ['admin']
    passwords = ['password', 'Password']
    
    if user in users and password_input in passwords:
        print(f'Welcome {user}!')
        print('You have successfully logged in!')
        print('Menu . . . ')
        print('1. View Account')
        print('2. Make a Transaction')
        print('3. Logout')
        
    elif user not in users:
        print('User not found. Try again...')
    
    elif password_input not in passwords:
        print('Incorrect password. Try again...')
    
    else: 
        print('Something went wrong. Please try again...')

# Example usage
login('admin', 'password')
