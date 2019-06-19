#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to print a report about a text file.
"""


# Define some functions for analyzing a string.

def nlines(text):
    """
    Count the number of lines in a string,
    by splitting on the newline character \n.
    
    arguments:
    text -- a string
    
    returns:
    int number of lines
    """
    return len(text.split('\n'))

def nwords(text):
    """
    Count the number of words in a string,
    by splitting on the space character.
    
    arguments:
    text -- a string
    
    returns:
    int number of words
    """
    return len(text.split())

# There are other more sophisticated ways of counting letters,
# but this one is fine for our purposes:
def nletters(text):
    """
    Count the number of letters in a string,
    using the string method isalpha() to recognize letters.
    
    arguments:
    text -- a string
    
    returns:
    int number of letters
    """
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

def ncharacters(text):
    """
    Count the number of characters in a string.
    
    arguments:
    text -- a string
    
    returns:
    int number of characters
    """
    return len(text)


# Define a format for the results.
# Later we will slot the results into the {} placeholders.
resultsFormat = """
file: {}
{} lines
{} words
{} letters
{} characters
"""


# Define the name of the file we want to work with.
filename = 'example.txt'

# Open the example file.
# The result is a file object with various methods.
f = open(filename)

# Read in the text from the file,
# using the read() method.
contents = f.read()

# Close the file.
f.close()


# Print the contents of the file just to check they are correct.
print(contents)

# Apply the functions we defined above,
# and put them into the results text.
results = resultsFormat.format(filename,
                               nlines(contents),
                               nwords(contents),
                               nletters(contents),
                               ncharacters(contents))


# Print out the results.
print(results)
