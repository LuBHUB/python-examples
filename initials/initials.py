#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program defines a group of related functions.
These functions are all based on the example of creating initials from names.
Once defined, these functions can be used again and again.
A section at the end of the program gives examples of using the functions.
"""


# We start simple, with a function to extract the first character from a string.
# A function is defined using the keyword 'def', followed by the function name.
# In parentheses we add any 'arguments' (i.e. inputs) that the function takes.
# The following indented commands form the body of the function.
# These commands will be executed when we 'call' (i.e. use) the function.
# The keyword 'return' defines what the function will return (i.e. what it will output).

def first_letter(word):
    return word[0]


# One function can be used within another. That is what we do next.
# We now use our first_letter() function inside another function.
# This new function is slightly more complex.
# It takes two arguments, a first name and a surname.
# It then returns the initials for the person named.
# In addition, we add one other important feature to this function: a 'dosctring'.
# A docstring is a piece of text that explains the behavior of a function or program.
# We should try to write these whenever we can, to help others use our programs.
# A triple-quoted string at the beginning of a function body becomes its docstring.
# See the section at the end of our program for an example of how docstrings are used.

def initials1(firstName, surname):
    """
    Get somebody's initials from their names.
    
    Required arguments:
    firstName -- str giving the person's first name
    surname   -- str giving the person's surname
    
    Returns:
    2-character str of initials
    """
    initial1 = first_letter(firstName)
    initial2 = first_letter(surname)
    return initial1 + initial2


# Our next function is again slightly more complex.
# What if somebody might have three names, or might have two?
# Our function then needs to work with either two or three arguments.
# We can make an argument optional by assigning it a default value, using =.
# Here we do this for the second surname.
# Then we check whether the user of the function entered a third name.
# We return a different value depending on whether they did or not.

def initials2(firstName, secondName, name3=''):
    """
    Get somebody's initials from either two or three names.
    
    Required arguments:
    firstName -- str giving the person's first name
    surname   -- str giving the person's second name
    
    Optional additional arguments:
    surname2  -- str giving a third name
    
    Returns:
    2- or 3-character str of initials
    """
    inits = first_letter(firstName) + first_letter(secondName)
    if name3:
        inits += first_letter(name3)
    return inits


# Our final function illustrates one more level of flexibility.
# We would now like a function that can accept an indefinite number of names.
# The * symbol indicates multiple possible arguments.
# All the arguments input to the function will then be gathered in one variable.
# By convention, this variable is called 'args'.
# Though we could give it another name if we wished.
# Our function can then loop through this variable or index entries in it.

def initials3(*args):
    """
    Get somebody's initials from their names.
    
    *args:
    multiple str arguments, each giving one name
    
    returns:
    str of initials with len equal to number of onput arguments
    """
    inits = ''
    for name in args:
        inits += first_letter(name)
    return inits


#%% Example uses of our functions

# Python has built-in function, some of which we have already met.
# These functions are always available for use.
# The len() function is one.
len('supercalifragilisticexpialidocious')

# Once we have defined functions of our own they can be used in the same way.
first_letter('supercalifragilisticexpialidocious')

# Functions can also have variables as inputs.
longWord = 'supercalifragilisticexpialidocious'
first_letter(longWord)

# Multiple arguments to a function are separated by commas.
initials1('amanda', 'bananarama')
initials2('amanda', 'mahatma', 'bananarama')

# Arguments that we have assigned a default value in the function definition are optional.
initials2('amanda', 'bananarama')

# We can view the docstring for a function using the help() function.
help(initials1)

# This works also for Python's own built-in functions.
help(len)

# A function whose arguments we have prefaced with * can take varyig number of arguments.
initials3('amanda')
initials3('amanda', 'bananarama')
initials3('amanda', 'mahatma', 'bananarama')
