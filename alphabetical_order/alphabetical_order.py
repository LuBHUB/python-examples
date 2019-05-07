#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to arrange some words in alphabetical order.
This program uses strings, lists, and a loop.
"""

# Get some words from the user.
words = input('Type in some words, separated by spaces: ')

# Use string methods to first convert the whole string into lowercase,
# then split it into a list of words.
# This could also be done in one line with:
# words = words.lower().split()
words = words.lower()
words = words.split()

# Strings are 'immutable'.
# They cannot be changed except by creating them anew.
# So to change a string we must re-assign it using =.

# Lists are 'mutable'.
# They can change when we use one of their methods.

# Sort the list using the list method sort().
# This method changes the list 'in place'.
# So there is no need to assign the result back into the variable with =.
words.sort()

# Print out the entries in the sorted list.
# A 'for' loop works with the entries of a list one by one in order.
print('Here are your words in alphabetical order:')
for w in words:
    print(w)
