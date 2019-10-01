#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A small example module for producing spoonerisms.
Use the spoonerize() function.
"""


def first_vowel(word):
    """
    Find the position of the first vowel in a word.
    
    argument:
    word -- a str word in which to search
    
    returns:
    int position
    """
    pos = 0
    for letter in word.lower():
        if letter in 'aeiou':
            break
        pos += 1
    return pos


def split_word(word):
    """
    Split a word into an initial consonant cluster and a remainder.
    
    argument:
    word -- a str word to split
    
    returns:
    list of str, with consonant cluster as item [0] and remainder as item [1]
    if word begins with a vowel, item [0] is an empty str
    """
    splitPos = first_vowel(word)
    return [word[:splitPos], word[splitPos:]]


def spoonerize(word1, word2):
    """
    Spoonerize two words, by swapping their initial consonant clusters.
    
    arguments:
    word1 -- str first word
    word2 -- str second word
    
    returns:
    str spoonerized phrase
    """
    split1 = split_word(word1)
    split2 = split_word(word2)
    return split2[0] + split1[1] + ' ' + split1[0] + split2[1]
