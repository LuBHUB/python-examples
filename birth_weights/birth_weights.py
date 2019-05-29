#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to explore the birth weights data.
Demonstrating very basic use of pandas, and numpy.
"""

# For more specialized tasks we need modules from outside the standard library.
# These have been developed by various groups of people in particular fields.
# Not all of these modules will be included in every installation of Python,
# so they may need to be installed first.
# But the most popular ones are often included.

# Modules can be imported under an 'alias', an alternative name.
# We can pick any such name we like, and then refer to the module by that name.
# This is done using the 'as' keyword.

# Many widely used modules have a conventional alias that everyone uses.
# We should try to stick to these conventions when we can,
# so that other Python users recognize which modules our program is using.

# The two modules used in this program both have conventional aliases.

import pandas as pd
import numpy as np


# The pandas module allows Python to work with tables of data.
# It can load these data from various file types.
# Here we use it to load an example table.
bw = pd.read_csv('birth_weights.csv')

# The resulting variable is a 'data frame'.
# A data frame stores data in rows and columns.
print(type(bw))

# The 'birth weights' data give the birth weights of some newborn children,
# along with various pieces of information about each child's mother.
print(bw)

# Indexing with the [] retrieves a single column from the data frame.
print(bw['Birth_weight'])

# numpy's statistical functions can summarize the data in a column.
print('Mean birth weight (kg):')
print(np.mean(bw['Birth_weight']))

# The .agg() method of a data frame produces a summary.
# ('agg' is short for 'aggregate', which means summarize.)
# The first input argument is a dictionary.
# The keys of the dictionary specify what columns we want to summarize.
# The values of the dictionary are lists of functions with which to summarize.
# For example the mean() and std() functions from numpy.
funcs = [np.mean, np.std]
summary = {'Birth_weight':funcs, 'Weight':funcs}
print(bw.agg(summary))

# The .groupby() method groups the data frame into separate categories.
# The first input argument is a list of columns to group by.
# If we then apply the .agg() method, our summaries are grouped.
print(bw.groupby(['Smoker', 'Hypertension']).agg(summary))
