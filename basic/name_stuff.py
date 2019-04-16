#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Our second example program.
    
A program to get the user's name and tell them some obvious things.
"""

# Get and store the user's name.
name = input('Name please: ')

# Print their name ten times.
# The multiplication operator * works on strings. It repeats them.
print('Hello')
print(name * 10)

# Print the first letter of their name.
# The square parentheses [] pick out single characters from a string.
# Python begins its numbering at 0, so 0 is the first character.
print('The first letter of your name is:')
print(name[0])

# Print out how many letters their name has.
# The len() function tells us how many characters a string contains.
# ('len' is short for 'length'.)
print('Your name has this many letters:')
print(len(name))
