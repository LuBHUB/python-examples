#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to check whether the user has the same name as me.
This program uses if statements.
"""

# Start by defining my name and surname as variables.
# This allows us to modify the program easily to use a different name.
myName = 'luke'
mySurname = 'tudge'

# Also define a list of interesting names.
# Later we check whether the user's name is in this list.
interestingNames = ['brunnhilda', 'morag', 'percival']

# Get the user's name and surname.
# At the same time, make the resulting strings lowercase.
name = input('Name: ').lower()
surname = input('Surname: ').lower()

# Now use a series of if... elif... statements,
# to check for one thing to say about the user's name.
# Each of these statements checks a logical condition.
# If the condition is met, then the indented line is executed.
# If not, then the next condition is checked, and so on.
if (name == myName) and (surname == mySurname):
    print('You have exactly the same name as me')
elif name == myName:
    print('You have the same first name as me')
elif surname == mySurname:
    print('You have the same surname as me')
elif name.startswith(myName[0]):
    print('Our names begin with the same letter.')
elif name in interestingNames:
    print('You have an interesting name.')
else:
    print('I have nothing interesting to say about your name.')

# Remember that a non-indented line will always be executed.
print('Goodbye.')
