#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A demonstration of reading and writing Python variables from and to a json file.
The example task is storing and retrieving a dictionary of word definitions.
"""

import json


# JSON stands for (J)ava(S)cript (O)bject (N)otation.
# JSON is a file format that stores data arranged in a particular way.
# The format is based on the JavaScript language,
# but is also common to many other languages, including Python.
# JSON files are a convenient way to store our Python variables,
# allowing them to be reloaded by another Python program,
# or if necessary by a program written in a different language.

# JSON files are usually stored as plain text.
# So in principle we can read them just as we read text files.
# If we do this for the example JSON file here,
# we see that the text is structured like Python code,
# with parentheses, commas, quotes, etc.
filename = 'example_vocab.json'
contents = open(filename).read()
print(contents)

# But reading the contents as text does not give us easy access to the data.
# The text is just text, not a dictionary or any other kind of Python variable.
type(contents)

# To load the data as a Python variable, we need the json module.
# The load() function loads data from a JSON file into a variable.
# The input argument is the open file.
vocab = json.load(open(filename))

# Now we have a proper Python variable and not just a string.
# In this case a dictionary, because the JSON file contains data enclosed in {}.
type(vocab)


# Now we can use the data in our program.
# The example here uses the dictionary to test our knowledge of arcane words.
score = 0
for word, definition in vocab.items():
    print('\n\n' + definition)
    answer = input('? ')
    if answer.lower() == word:
        print('Correct!')
        score += 1
    else:
        print('Wrong! The word is {}.'.format(word))
print('\nYou remembered {} out of {} words.'.format(score, len(vocab)))


# We can also write Python variables to a JSON file.
# The example here updates the dictionary with new definitions from the user,
# then saves the modified dictionary to a new JSON file.
while True:
    word = input('Enter a new word to store (or press return to quit): ')
    if word:
        definition = input('Enter the definition to store: ')
        vocab[word] = definition
    else:
        break

# Somewhat counterintuitively, the function for writing to a JSON file is dump().
# We are 'dumping' the Python data into a file.
# The first input argument is the variable we want to save.
# The second input argument is a file open in write mode.
newFilename = 'my_vocab.json'
json.dump(vocab, open(newFilename, mode='w'))

# We can check that writing has worked by deleting our variable and reloading it.
del vocab
vocab = json.load(open(newFilename))
print(vocab)
