#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A short demonstration of importing modules from the standard library.
Featuring:
webbrowser
math
random
os
"""

# Basic Python is limited in its capabilities.
# But there are many ready-made modules that add extra functions.
# The core set of these modules is included in almost any Python installation.
# It is known as the 'standard library'.
# We can import these modules into our programs in order to use their functions.
# This program demonstrates just a few modules from the standard library.


#%% webbrowser

import webbrowser

# The webbrowser module provides a function that opens a webpage.
# The webpage will open in your default web browser.
# Let's use it to open the Python documentation page on the standard library.
webbrowser.open('https://docs.python.org/3/library/')

# The same function can open a file.
# It opens it using your default program for that file type.
webbrowser.open('example.jpg')


#%% math

import math

# The dir() function tells us what an imported module contains.
print('Contents of the math module:')
print(dir(math))

# We can see that the math module contains various mathematical functions.
# For example the factorial function.
print('7 factorial is:')
print(math.factorial(7))

# Most of these are the sort of functions that we could define ourselves.
# For example:

def factorial(x):
    answer = 1
    for i in range(1, x+1):
        answer *= i
    return answer

print('7 factorial is:')
print(factorial(7))

# But it is more convenient to use a predefined function if one exists.
# These are often more efficient and more robust than those we write ourselves.
# For example, our factorial() function above doesn't handle negative numbers correctly.

# The math module also contains some variables defining mathematical constants.
# For example pi:
print('Here is some pi:')
print(math.pi)


#%% random

import random

# The random module generates random numbers in various ways.

print('A random integer:')
print(random.randint(1, 10))

print('Random entries from a list:')
print(random.sample(['fast', 'cheap', 'good'], 2))

print('A random number drawn from a normal distribution:')
print(random.normalvariate(100, 15))


#%% os

import os

# The os module contains functions for managing directories on the computer.
# (OS stands for Operating System.)

# We can use it to create a new directory:
os.mkdir('example_folder')

# To list the contents of the current directory:
print(os.listdir())

# Or delete a directory:
os.rmdir('example_folder')
print(os.listdir())
