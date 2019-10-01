#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program demonstrates importing and using a module.
The accompanying module is in the file 'wordplay.py'.
It is used here to spoonerize two words that the user enters.
"""

# We import modules using the 'import' keyword.
# The name of the module is the name of the file.
import wordplay

# Any variables or functions defined in the module are now available.
# We can use them in this program without having to define them again here.
# The contents of an imported module are kept in a separate 'namespace'.
# We access the contents of a namespace using a dot '.'
# So to get the help for the spoonerize() function in the wordplay module:
help(wordplay.spoonerize)

# Now we will use this function.
# First get two words from the user.
print('Think of a two-word phrase.')
word1 = input('Type the first word: ')
word2 = input('Now type the second word: ')

# Then create the spoonerism.
result = wordplay.spoonerize(word1, word2)

# Then print it out.
print('Here is the phrase spoonerized:')
print(result)
