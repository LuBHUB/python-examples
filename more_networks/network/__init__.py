#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An extended version of the network module.
Contains two submodules, each of which defines a Network and DirectedNetwork class.
The two submodules each use different data structures for the implementation.

more_network.adj_array:
The implementation using a numpy array to represent a network as an adjacency matrix.

more_network.dict_of_sets:
The implementation representing the network as a dictionary of sets.
"""

from os import path


# An __init__.py file will often be empty except for a docstring.
# But we can include code here as well.
# This code will be executed the first time the overall module is imported.
# Any variables we define here will be available as attributes of the module.

# In more complex cases, we may need to run code to set up the module.
# But in this case we just do a couple of things for illustration purposes:


# Print a welcome message.
print('Welcome to the network module.')

# Find the path to the example image file.
EXAMPLEIMAGE = path.join(path.dirname(path.abspath(__file__)), 'data', 'example.png')
