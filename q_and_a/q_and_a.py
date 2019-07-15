#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to collect and then repeat some information from the user.
This program uses lists, dictionaries, and loops.
"""

# Begin by defining some topics to ask the user about.
topics = ['name', 'nationality', 'favorite color']

# Set up an empty dictionary to store the answers.
info = {}

# Fill the dictionary using a loop going through the question list.
# This is a more complex loop with a few operations in each iteration.
# For each topic format it into a neat question using string formatting.
# Then ask the question.
# Then store the answer in the dictionary.
# Use the topic as the key and the answer as the value.
for t in topics:
    question = 'What is your {}? '.format(t)
    answer = input(question)
    info[t] = answer

# Go through the dictionary of information and print out the items.
# A loop through a dictionary works through its keys.
# So use each key to get the corresponding value.
# Then print key and value as a nice formatted string.
for x in info:
    msg = 'Your {} is {}.'.format(x, info[x])
    print(msg)
