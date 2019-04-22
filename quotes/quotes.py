#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Work with quoted text in strings.
"""

import re


# The start of quoted text:
# Either of the quote characters, preceded by whitespace or start of string.
# (Achieved as 'not non-whitespace'.)
OPENQUOTE = r'(?<!\S)("|“)'

# The end of quoted text:
# Either of the quote characters, preceded by non-whitespace.
CLOSEQUOTE = r'(?<=\S)("|”)'


def find(text, word='', case=False):
    """
    Find quotes within a string.
    
    Required arguments:
    text -- string in which to search
    
    Optional keyword arguments:
    word -- word that quotes must contain
            defaults to '' (i.e. find all quotes)
    case -- whether to match the case of the word
            defaults to False (i.e. case-insensitive search)
    
    Returns:
    generator of quote strings
    
    Matches either straight ("") or curly (“”) quotes.
    Does not match single quotes ('').
    Multiple occurrences of the word within the same quote constitute a single match.
    If word occurs in a quote within a quote, matches the inner quote.
    
    It is assumed that:
    Opening quote characters are always preceded by whitespace or the start of the string.
    Quoted text always ends with a non-whitespace.
    """
    
    if case:
        flags = 0
    else:
        flags = re.IGNORECASE
    
    # The target word:
    # The word preceded and followed by a non-word character.
    # (This excludes other words that contain the target word.
    if word:
        target = r'(?<=\W){}(?=\W)'.format(word)
    else:
        target = ''
    
    # Possible other text within the quote:
    # Any string of characters other than the quote characters.
    filler = '[^"“”]*'
    
    pattern = OPENQUOTE + filler + target + filler + CLOSEQUOTE
    
    # Yield just the matched text from each match object.
    for match in re.finditer(pattern, text, flags):
        yield match[0]


def remove(text, ellipsis=' [...] ', invert=False):
    """
    Remove quotes from a string.
    
    Required arguments:
    text -- string from which to remove quotes
    
    Optional keyword arguments:
    ellipsis   -- string to insert in place of quoted text
                  defaults to ' [...] '
    invert     -- if True, remove unquoted text
                  defaults to False
    
    Returns:
    modified string
    """
    
    pattern = OPENQUOTE + '.*?' + CLOSEQUOTE
    
    if invert:
        return ellipsis.join([match[0] for match in re.finditer(pattern, text)])
    
    return re.sub(pattern, ellipsis, text)


if __name__ == '__main__':
    
    exampleText = open('example.txt').read()
    exampleShortText = exampleText.split('\n')[0]
    exampleWord = 'Fuck'
    
    # Test find().
    print('Case insensitive search for "{}":'.format(exampleWord))
    for quote in find(exampleText, exampleWord):
        print(quote)
    
    # Test case-sensitive find().
    print('\nCase sensitive search for "{}":'.format(exampleWord))
    for quote in find(exampleText, exampleWord, case=True):
        print(quote)
    
    # Test remove().
    print('\nRemove quotes:')
    print(remove(exampleShortText))
    
    # Test remove() inverted.
    print('\nRemove non-quotes:')
    print(remove(exampleShortText, invert=True))
