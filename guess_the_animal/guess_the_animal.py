#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to play a game of 'guess the animal'.
With hints and a limited number of rounds.
This program uses a loop with the break keyword.
"""

# Start by defining the correct animal.
animal = 'african swallow'

# And define a list of hints.
# Since the ist is long, we can break it across several lines.
# This is juts for clarity and doesn't affect the workings of the program.
hints = ['weighs five ounces',
         'beats its wings 43 times per second',
         'is not migratory',
         'has dorsal guiding feathers',
         'can carry a coconut',
         'is not European']

# Print an introductory message.
print("I'm thinking of an animal.")

# Loop through the list of hints.
for h in hints:
    
    # Give the hint.
    print('Hint: It {}.'.format(h))
    
    # Ask for a guess.
    guess = input('What is it? ')
    
    # Strip away any spaces the user typed by accident,
    # and make their answer lowercase.
    guess = guess.strip().lower()
    
    # Check their guess and break out of the loop if they got it right.
    if guess == animal:
        print('Correct!')
        break
    else:
        print("No, that's not it.")

# Print a final message revealing (or confirming) the answer.
print('It was the {}.'.format(animal))
