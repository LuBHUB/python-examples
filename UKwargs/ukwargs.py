#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decorate functions so they accept UK-spelling keyword arguments \
if the function definition defines US-spelled keywords.
This is probably not a very Pythonic thing to do, or even a good idea.
But it is the first novel (to my knowledge) example I could think of for decorators.
"""

import functools
import json


SPELLINGSFILE = 'spellings.json'
with open(SPELLINGSFILE) as f:
    SPELLINGS = json.load(f)


def respell_kwargs(func):
    """
    Wrap a function so that keywords may be entered in UK spelling.
    For example, if func defines a keyword argument called color, \
    respell_kwargs(func) accepts either 'color=...' or 'colour=...'
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        respelled_kwargs = {SPELLINGS.get(key, key):value for key, value in kwargs.items()}
        return func(*args, **respelled_kwargs)
    return wrapper


# Debugging tests.
if __name__ == '__main__':
    
    @respell_kwargs
    def test_func(color):
        """docstring OK"""
        return color
    
    # Check docstring is not overwritten by wrapper.
    print(test_func.__doc__)
    
    # Check original spelling is accepted.
    print('original spelling', test_func(color='OK'))
    
    # Check variant spelling is accepted.
    print('variant spelling', test_func(colour='OK'))
