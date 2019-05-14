#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to play a game of 'guess the number'.
This program uses if statements, a while loop, and a try... except statement.
"""

# Start by defining the number the user has to guess.
answer = 42

# Print out a short introduction to the game,
# then ask for their first guess.
print("I'm thinking of a number between 1 and 100.")

# To get things started, assume an incorrect guess to begin with.
# This is necessary in order that the guess variable be defined when we use it below.
guess = 0

# A while loop runs for as long as a given condition is true.
# Here we use the condition that the user's guess does not match the answer.
# The contents of the while loop are repeated until this condition is false.
while guess != answer:
    
    # Since this loop is a bit longer, we have many indented lines.
    # All of the indented lines here belong to the while loop.
    # So they will all be run over and over until the loop ends.
    
    # The first thing to do is to ask for a new guess.
    guess = input('Guess the number: ')
    
    # Then convert their string input to an integer.
    # This time, we do so slightly more 'cautiously'.
    # A try statement tries to run some Python commands.
    # But if an error arises, it doesn't stop our program as usual.
    # Instead, the commands under the except statement are run.
    # Here we use the except statement to print a warning,
    # and to continue on to the next run of the while loop.
    try:
        guess = int(guess)
    except:
        print('Not a valid number.')
        continue
    
    # If we have reached this part of the program,
    # it means that we have a valid guess.
    # So now we give a hint using some if statements.
    if guess < answer:
        print('Too low.')
    elif guess > answer:
        print('Too high.')

# Remember that once we stop indenting our commands, the loop is over.
# So the following command will only be executed once the loop has finished.
# This can only occur if the user guessed correctly.
# So we finish by printing a congratulatory message.
print('Correct!')
