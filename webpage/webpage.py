#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to retrieve some text from a webpage.
Using requests and bs4.
"""

import webbrowser
import requests
import bs4


# The requests module provides functions for retrieving data from the internet.
# Its get() function gets (or tries to get) a webpage.
url = 'http://www.mind-and-brain.de/home/'
page = requests.get(url)

# Note that this is different from what the webbrowser module does.
# Whereas webbrowser opens the webpage in our browser,
# requests gets the webpage into our Python session for analysis.

# Behind the scenes, our computer sends a 'request' for the webpage.
# The server where the webpage is stored responds to the request.
# If all goes well, it will send us the webpage.
# We should check first whether our request could be fulfilled.
# The status_code attribute of the resulting variable tells us this.
# Code numbers from 200 to 299 indicate a successful request.
print(page.status_code)

# There is also a more human-readable message to go with the code.
print(page.reason)

# Codes from 400 to 499 indicate a failed request.
# For example a page that does not exist:
page2 = requests.get('http://www.mind-and-brain.de/dirks_holiday_photos')
print('{}: {}'.format(page2.status_code, page2.reason))

# You can read a full list of status codes here:
webbrowser.open('https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml')

# If successful, the text content of the webpage is in the text attribute.
print(page.text)

# The format of the text is usually html.
# This is normal text but interspersed with 'tags'.
# These tags give our web browser information about how to display the page.
# If we want to extract some information from the webpage in Python,
# we will need to navigate through these tags to find the parts we want.

# The bs4 module provides functions that make it easier to search through html.
# bs stands for Beautiful Soup.
# A BeautifulSoup object stores html text, along with methods for searching it.
# We can create such an object from our html text.
content = bs4.BeautifulSoup(page.text, features='html.parser')

# If we examine the resulting variable we see it has many methods.
# Lots of these are methods for searching or retrieving parts of the text.
print(dir(content))

# The simplest and most generally useful method is find_all().
# This method finds all html tags of a certain type.
# To use this method, we must know what we are looking for.
# In simple web pages, the 'p' tag marks a 'paragraph' of text.
# So if we search for this tag we may get text content.
paras = content.find_all('p')

# The result is a list of the chunks of tagged text.
for p in paras:
    print(p)

# For a more specific search we can specify what 'attributes' to search for.
# An attribute is an extra piece of information included in an html tag.
# Often the 'class' attribute tells us something about the purpose of the text.
# We can specify html attributes using a dictionary as the input argument.
# The keys of the dictionary are the attribute names, and the values the attribute values.
# In the html tag this appears as, for example: class="bodytext"
# So in a Python dictionary this would be: {'class':'bodytext'}

# For our example webpage, there is only one piece of text that matches the pattern
# 'p' tag with the class attribute 'bodytext'.
paras = content.find_all('p', attrs={'class':'bodytext'})
print(len(paras))

# The result includes both the tag and the text that it encloses.
print(paras[0])

# If we want just the text it is in the text attribute of the result.
pageText = paras[0].text
print(pageText)

# Once we have gathered some text we may then go on to do some analysis.
# Below is a very simple example:

# Count up parts of the text.
nChars = len(pageText)
nWords = len(pageText.split(' '))
nSents = len(pageText.split('.'))

# Define a neatly-arranged printed output.
results = """Main paragraph from webpage:
{}

{} characters
{} words
{} sentences
"""

# Print it with the corresponding information inserted.
print(results.format(url, nChars, nWords, nSents))
