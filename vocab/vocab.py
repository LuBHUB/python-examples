#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to store words in a text file.
For example in order to store newly-learned vocabulary.
"""


# Define the name of the data file.'to write to.
filename = 'vocab.txt'

# Open the file in 'append' mode.
# This will create the file if it does not exist,
# or add new text to it at the bottom if it does.
f = open(filename, mode='a')

# Start a while loop to run until we reach a 'break' statement.
while True:
    
    # Ask the user for a word.
    word = input('Enter a word to store (or press return to quit): ')
    
    # If they entered a word, then store it.
    # Add a newline character so that the next word is on the next line.
    # If not, then stop the loop.
    if word:
        f.write(word + '\n')
    else:
        break

# Close the file.
# (Not always essential but a good habit to get into.)
f.close()


# Open the file and read it, to confirm what words have been stored so far.
# We can apply the read() method directly to the result of open().
# This is a convenient shortcut if we want to read the whole file just once.
words = open(filename).read()

# Print out all the words.
print('Words stored so far:')
print(words)
