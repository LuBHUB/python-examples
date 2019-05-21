#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program imports the initials module that we wrote.
It then uses some of the functions in that module to tell the user their initials.
"""

import initials


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

# Print the initials using the initials3() function.
print('Your initials are:')
print(initials.initials3(*names))
