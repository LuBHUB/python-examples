#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program imports the initials module that we wrote.
It then uses some of the functions in that module to tell the user their initials.
"""

# We can import the contents of another Python program into our current one.
# Any functions or variables defined in that program are then available for our current one.
# We can import using the 'import' keyword and the name of the other program.

import initials


# The contents of the imported program are available under its 'namespace'.
# To use them, we preface them with the name of the imported program and a dot.
# For example to get help with the 'initials3' function from the initials program:
help(initials.initials3)


# Print an introductory message.
print('Tell me all your names.')

# Create a list to store the user's names.
names = []

# Start a never-ending loop using 'while'.
while True:
    
    # Ask the user for a name.
    name = input('Next name (or just press enter to stop): ')
    
    # If they entered something, add it to the list of names.
    # Otherwise, break out of the loop.
    if name:
        names.append(name)
    else:
        break

# Print the initials using the imported initials3() function.
# (Remember to preface with the name of the imported program.
print('Your initials are:')
print(initials.initials3(*names))
