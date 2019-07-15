#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to tell the user some more things about their name.
This program uses string methods.
"""

# Get and store the user's name.
name = input('Name please: ')

# A method is a function that is 'bound' to one type of variable.
# String variables have many methods.
# To use a method for a variable:
# type the variable name
# type a dot .
# type the name of the method
# then type the parentheses (as we do for any other function)
# For example, the lower() method gives us a lowercase version of a string.
print('This is your name in lowercase:')
print(name.lower())

# The capitalize() method just puts the first character in uppercase.
print('This is your name capitalized:')
print(name.capitalize())

# Other methods are more complex and require some input in the parentheses.
# For example the format() method inserts something into the string
# at the place where curly braces {} appear in the string.
# (There is a little bit more to this, but that is the basic idea.)
phrase = 'Goodbye {}, see you later.'
print(phrase.format(name))
