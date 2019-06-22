#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Some functions for alternative methods of accomplishing basic tasks.

Functions with similar names accomplish the same task in different ways.
These can be compared for profiling or demonstration purposes.
For example with timeit, line_profiler, or memory_profiler.

A function for comparing the execution time of two functions is also provided.
"""

import functools
import os
from timeit import timeit
import numpy



#%% loop vs comprehension


def make_list_with_loop(n):
    """
    Return a list of the first n square numbers.
    This version appends to the list in a loop.
    Compare with: make_list_with_comprehension
    """
    squares = []
    for i in range(n):
        squares.append(i**2)
    return squares


def make_list_with_comprehension(n):
    """
    Return a list of the first n square numbers.
    This version creates the list with a comprehension.
    Compare with: make_list_with_loop
    """
    return [i**2 for i in range(n)]



#%% disk write vs memory write


TEMPFILENAME = '.temp.txt'


def write_string_on_disk(n):
    """
    Write a string of n digits to a temporary file.
    This version writes each digit to the file in a separate open and write.
    Compare with: write_string_in_memory
    """
    with open(TEMPFILENAME, mode='w') as f:
        for i in range(n):
            f.write(str(i % 10))
            f.flush() # (ensures writing occurs on every iteration)
    os.remove(TEMPFILENAME)


def write_string_in_memory(n):
    """
    Write a string of n digits to a temporary file.
    This version first grows the string in memory then writes it to file.
    Compare with: write_string_on_disk
    """
    text = ''
    for i in range(n):
        text = text + str(i % 10)
    with open(TEMPFILENAME, mode='w') as f:
        f.write(text)
    os.remove(TEMPFILENAME)



#%% array copy vs no copy


def calculate_via_copies(n):
    """
    Return the density of the standard normal distribution for n values \
    linearly spaced between -3 and 3.
    This version allocates intermediate arrays.
    Compare with: calculate_without_copies
    """
    x = numpy.linspace(-3, 3, n)
    xSq = x**2
    halfxSq = xSq / 2
    negHalfxSq = -halfxSq
    eToTheNegHalfxSq = numpy.e**negHalfxSq
    factor = 1 / numpy.sqrt(2 * numpy.pi)
    return factor * eToTheNegHalfxSq
    
    
def calculate_without_copies(n):
    """
    Return the density of the standard normal distribution for n values \
    linearly spaced between -3 and 3.
    This version allocates no intermediate arrays.
    Compare with: calculate_via_copies
    """
    return (1 / numpy.sqrt(2*numpy.pi)) * numpy.e**-(numpy.linspace(-3, 3, n)**2 / 2)



#%% comparison function


def compare(func1, func2, number, *args, **kwargs):
    """
    Print a comparison of the execution times of two functions func1 and func2.
    Using timeit.timeit(func, number=number).
    Any additional arguments are passed on to both functions.
    """
    funcs = [func1, func2]
    names = [func.__name__ for func in funcs]
    t = [timeit(functools.partial(func, *args, **kwargs), number=number) for func in funcs]
    diff = t[1] - t[0]
    if diff < 0:
        names.reverse()
    results = '{} faster than {} by:\n{} s\n'.format(*names, abs(diff))
    print(results)



#%% quick tests


if __name__ == '__main__':
    
    n = 9000
    number = 1
    compare(make_list_with_loop, make_list_with_comprehension, number, n)
    compare(write_string_on_disk, write_string_in_memory, number, n)
    compare(calculate_via_copies, calculate_without_copies, number, n)
