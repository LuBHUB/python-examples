#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Our first example program.

We can use this space here to provide a short description of our program.
For example:

A program to get a user's age and tell them their age in one year.
"""

# We use comments to provide information about the workings of our program.
# Comments are preceded by #.
# This tells Python not to try to run the comment line as Python commands.

# The first thing we do in this program is get the user's age.
# The input() function prints a prompt at the console.
# Whatever the user types there becomes the output of the input() function.
# In this case, we store the output in a variable that we call 'age'.
age = input('Age please: ')

# Any user input collected with input() comes in the form of a string.
# ('string' means text).
# This is the case even if the user types numbers.
# Python is strict about treating data as numbers or text.
# We can't do math with a piece of text.
# So first we must convert the user's input into an 'int'.
# ('int' means integer, i.e. a whole number).
age = int(age)

# Now we can use the print() function to display some printout.
# Anything we print will be displayed in the console.
# Here we print first some explanatory text.
# Text in Python must be enclosed in quotes ''.
# Then we print the answer, using the 'age' variable that we assigned above.
print('In one year you will be:')
print(age + 1)
