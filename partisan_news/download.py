#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script to download and process the BuzzFeed-Webis fake news corpus.
"""

from glob import glob
from os import path
import zipfile

from bs4 import BeautifulSoup
import requests


#%% Download

# Web address.
url = 'https://zenodo.org/record/1239675/files/'
zipfilename = 'articles.zip'

# Retreive.
print('retrieving {} from {}'.format(zipfilename, url))
r = requests.get(url + zipfilename)
print('{}: {}'.format(r.status_code, r.reason))

# Write to local file.
with open(zipfilename, mode='wb') as f:
    f.write(r.content)


#%% Extract

# Unzip.
print('extracting')
with zipfile.ZipFile(zipfilename) as zf:
    zf.extractall()

# Get list of files.
subfolder = 'articles'
xmlfilenames = glob(path.join(subfolder, '*.xml'))
print('{} files extracted'.format(len(xmlfilenames)))


#%% Convert to plain text

# Open new text files.
output_encoding = 'utf-8'
open('mainstream.txt', mode='w', encoding=output_encoding)
open('partisan.txt', mode='w', encoding=output_encoding)

# Map them to the orientation labels in the xml files.
mapping = {'mainstream': 'mainstream.txt',
           'right': 'partisan.txt',
           'left': 'partisan.txt'}

# Read the body text of each xml file into the relevant text file.
print('writing to text files')
n_texts = 0
for xmlfilename in xmlfilenames:
    contents = BeautifulSoup(open(xmlfilename).read(), features='html.parser')
    orientation = contents.find('orientation').get_text()
    text = contents.find('maintext').get_text()
    if text:
        with open(mapping[orientation], mode='a', encoding=output_encoding) as f:
            f.write(text + '\n')
        n_texts += 1
    else:
        print('{} empty!'.format(xmlfilename))
print('{} texts written'.format(n_texts))
