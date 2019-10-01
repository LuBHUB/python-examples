#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to search in a text file.
Prints the first line in a file that contains a given phrase.
"""


# Ask the user to choose a word or phrase to search for.
target = input('Word or phrase to search for: ')

# Open the example file.
f = open('example.txt')

# Define a default empty result if the search target is not found.
result = ''

# Go through each line.
for line in f:
    
    # If the word is found, store it and stop searching.
    # (Make the search independent of case).
    if target.lower() in line.lower():
        result = line
        break

# Close the file.
f.close()

# Print the result if one was found.
if result:
    print('First line containing "{}": {}'.format(target, result))
else:
    print('"{}" not found.'.format(target))
