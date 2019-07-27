#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to retrieve a dictionary of US-UK spelling differences from the web.
"""

import json
import requests
import bs4


#%% Web address

url = 'http://www.tysto.com/uk-us-spelling-list.html'

# Check the browser view of the webpage for debugging purposes:
#import webbrowser
#webbrowser.open(url)


#%% Connect

r = requests.get(url)
msg = '{}: {}, {}'.format(url, r.status_code, r.reason)
if not (200 <= r.status_code < 300):
    raise requests.exceptions.RequestException(msg)
else:
    print(msg)


#%% Parse html

content = bs4.BeautifulSoup(r.text, features='html.parser')

# Column headings giving the two languages:
# bold text ('b') of class 'HeadingsSub'
headings = content.find_all('b', attrs={'class':'HeadingsSub'})
languages = [x.get_text() for x in headings]

# Columns of words:
# table cells ('td') in the table row ('tr') of class 'Body'
body = content.find('tr', attrs={'class':'Body'})
cells = body.find_all('td')
words = [x.get_text().split() for x in cells]


#%% Format to dictionary

cols = {x:languages.index(x) for x in languages}

# UK spelling as key, US spelling as value.
# i.e. optimized for looking up US given UK.
spellings = {x:y for x, y in zip(words[cols['UK']], words[cols['US']])}

# Some bits of punctuation find their way into the word lists.
spellings = {x:y for x, y in spellings.items() if x.isalpha() and y.isalpha()}


#%% Feck! Arse!

# The omission of these vital words is truly baffling,
# especially since 'sodomise/sodomize' is in there.
spellings['feck'] = 'fuck' # (I know, I know, it's not quite the same)
spellings['arse'] = 'ass'


#%% Save to JSON

filename = 'spellings.json'

# Indent and sort keys just so the file reads clearly in a text editor.
with open(filename, mode='w') as f:
    json.dump(spellings, f, indent=0, sort_keys=True)


#%% Check

print(open(filename).read())
