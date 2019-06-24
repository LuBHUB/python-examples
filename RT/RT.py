#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A short demonstration of psychopy, testing the speed of the user's reactions.
The user sees letters and must press the corresponding letter key.
"""

import webbrowser

# psychopy contains various modules for handling different things.
# We import here only those that we need:
# visual -- opens windows and displays things in them
# core   -- does a few basic things, including timing when things happen
# event  -- collects 'events' from the keyboard and mouse
from psychopy import visual, core, event


#%% Psychopy setup

# The visual module's main starting point is the Window object.
# Window() opens a window and stores a reference to it in a Python variable.
# The variable that we assign here is our program's way of referring to the window.
win = visual.Window()

# The visual module also provides various 'Stim' objects.
# These create some kind of visual stimulus such as a shape or image.
# Here we create a text stimulus.
# The first input argument is the name of the window for the stimulus.
# We can additionally specify its color, position and many other things.
# Positions are by default given in a coordinate space with center at (0,0),
# and corners at (1,1) (1,-1) (-1,-1) and (-1,1).
stim = visual.TextStim(win, color='green', pos=(0, 0))

# The Clock object from the core module times things.
# The Clock has methods:
# .reset() reset the timer
# .getTime() get the time elapsed (in seconds) since the last reset
timer = core.Clock()


#%% General setup

# Create a list of letters that the user will see on the screen.
# (If they are clever, they may detect a subtle pattern.)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# We will usually want to save the user's responses to a file.
# There are a few ways of doing this.
# But here we use the simplest and open a text file to write them into.
resultsFilename = 'results.csv'
f = open(resultsFilename, mode='w')

# Write a header line into the file,
# with column names for the letter displayed, response, and Reaction Time.
f.write('Letter,Answer,RT\n')

# It is convenient to also define a format for the lines of the results file.
# Doing so at this point in our program allows us to compare this format easily with the header.
# (Though later we will see alternative ways of handling this.)
lineFormat = '{},{},{}\n'


#%% Main loop

# We now go through all the letters that we want to show.
for letter in letters:
    
    # The attributes of stimuli can be changed repeatedly.
    # Here we change the 'text' attribute of our stimulus.
    # We assign into it the current letter
    # (in uppercase for EXTRA PSYCHOLOGICAL IMPACT).
    stim.text = letter.upper()
    
    # Stim objects are not drawn until we request it.
    # We can do so with the .draw() method of the Stim object.
    stim.draw()
    
    # And even once things are drawn, they are not actually shown in the window,
    # until we request that the current drawing be shown.
    # We can do so with the .flip() method of the Window object.
    win.flip()
    
    # Right after displaying the current letter we reset our Clock object.
    # This means that subsequent events are timed relative to this moment.
    timer.reset()
    
    # The waitKeys() function from the event module waits for the user to press a key.
    # If we additionally input our Clock object as the timeStamped argument,
    # the output of this function will iclude the timing of the key press according to our Clock.
    result = event.waitKeys(timeStamped=timer)
    
    # The result of a timed key press is a list.
    # This list is a list of the keys that were pressed.
    # Typically this will only be one key.
    # But even in this case the result is a list with just one entry.
    # Each entry in the list is itself a list.
    # This list contains the name of the key pressed as its first entry
    # and the time of the key press as its second entry.
    # Given this knowledge, we can extract the key name and timing thus:
    key = result[0][0] # ('first entry of first entry')
    rt = result[0][1] # ('second entry of first entry')
    
    # The final action of our loop is to write the results to file.
    # We use the line format string we defined during the setup above.
    line = lineFormat.format(letter, key, rt)
    f.write(line)
    
    # In addition just for illustration purposesg print the line to the console.
    print(line)


#%% Tidy up

# We should tidy up by closing the window we opened.
# This can be done with the .close() method of the Window object.
# If we don't do this then the window will stay open after the end of our program.
win.close()

# We should also close the results file.
f.close()

# As a little bonus, we try to open the results file,
# using our default spreadsheet program.
# (Though this can get annoying when repeatedly testing the program.)
webbrowser.open(resultsFilename)
