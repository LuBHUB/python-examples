#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Another Psychopy demonstration, using image files.
The user must identify pictures of crabs and lobsters.
"""

import os

from psychopy import visual, core, data, event


#%% General setup

# We will often want to record the meaning of the key the subject pressed.
# We can use a dictionary to assign meanings to keyboard keys.
# If we access this dictionary using the name of the key,
# we will get back its assigned meaning.
keyMeanings = {'lshift':'crab', 'rshift':'lobster',
               'q':'quit'}

# We can limit the keys that the subject is allowed to press,
# and ensure that only these keys are recorded.
# Here we will set up a list of allowed keys.
# It contains the keys we defined above.
allowedKeys = keyMeanings.keys()

# If we want to get extra information about the subject,
# we can enter it into the console at the start of the experiment.
# For example, we might want to record an ID number.
subjectID = input('Subject ID: ')

# This experiment involves image files.
# Let's define a list of the image files.
# We could also do this more flexibly by searching in the images folder.
# But for now we keep it simple.
imageFiles = ['crab_1.jpg',
              'crab_2.jpg',
              'crab_3.jpg',
              'lobster_1.jpg',
              'lobster_2.jpg',
              'lobster_3.jpg']


#%% Psychopy setup: Trials

# We can define the trials of the experiment in a spreadsheet,
# and then load them into our program.
# The importConditions function from Psychopy's data module does this.
# The result is a list of dictionaries.
# Each dictionary is one type of trial.
# Its keys and values are the names and values of variables in the experiment.
# Here the two variables are just the name of the image the subject will see,
# and the type of that image (i.e. 'crab' or 'lobster').
trialTypes = data.importConditions('trials.csv')

# A Psychopy 'TrialHandler' can organize the trials for us.
# It takes care of several things:
# * repeating each trial type a given number of times
# * randomizing the order of the trials
# * recording responses
# We input the list of trial types we loaded above,
# along with the required number of repeitions (here just 2),
# and the randomization method.
# The extraInfo argument accepts a dictionary of additional information.
# We can use this to record information that is constant for the whole session,
# such as the subject ID, age, date and time, etc.
# This extra information will be saved along with the trial-by-trial data.
trials = data.TrialHandler(trialTypes, nReps=2, method='random',
                           extraInfo={'Subject':subjectID})


#%% Psychopy setup: Window

# Open a window.
win = visual.Window()

# We should pre-load the images before beginning the main loop,
# because loading images is somewhat time-consuming.
# Images are loaded as Psychopy image 'stims' for a specified open window.
# A good way to organize the images is as a dictionary.
# The keys of the dictionary are the image names,
# and the values are the Psychopy image stims.
# We need the path module from os to 'join' the image folder to the image file.
images = {}
for fileName in imageFiles:
    filePath = os.path.join('images', fileName)
    images[fileName] = visual.ImageStim(win, image=filePath)

# Start a timer.
timer = core.Clock()


#%% Main loop

# The TrialHandler is 'iterable' (i.e. it can be looped through).
# The TrialHandler gives us some trial information on each iteration.
# This trial information comes in the form of a dictionary,
# informing our program what should be displayed/pressed/etc for that trial.
# The order is already randomized.
for t in trials:
    
    # First draw the current image.
    # We get the image from the dictionary we defined above,
    # in conjunction with the information the TrialHandler gives us.
    images[t['Image']].draw()
    
    # Show it and start timing.
    win.flip()
    timer.reset()
    
    # Wait for a key press.
    # Restrict the recorded keys to those we defined above.
    keyPress = event.waitKeys(keyList=allowedKeys, timeStamped=timer)
    
    # Get the meaning of the key pressed,
    # using the dictionary of key meanings.
    response = keyMeanings[keyPress[0][0]]
    
    # Get the reaction time.
    rt = keyPress[0][1]
    
    # Check whether the key meaning matches the image type for this trial.
    if response == t['Type']:
        correct = 'yes'
    else:
        correct = 'no'
    
    # Store the results in the TrialHandler.
    # Its addData() method stores new data.
    # The first argument is the string name of the piece of information.
    # This will be used as the name of the column in the output data file.
    # The second argument is the value we want to store for this trial.
    trials.addData('Response', response)
    trials.addData('Correct', correct)
    
    # If the quit key was pressed, break out of the loop.
    if response == 'quit':
        break


#%% Tidy up

# Close the window.
win.close()

# Save the results to a file for this subject.
# The TrialHandler has many methods for saving results.
# saveAsWideText() is a good one.
# This saves a text file in which each row is one trial.
# To make this a csv file, we can specify the comma as the 'delimiter'.
# By default the results are appended to the file if it exists.
# We might not want this.
# The fileCollisionMethod argument says what to do if the file already exists.
resultsFilename = 'results_{}.csv'.format(subjectID)
results = trials.saveAsWideText(resultsFilename, delim=',',
                                appendFile=False, fileCollisionMethod='overwrite')

# In addition, saveAsWideText returns a pandas DataFrame of results.
# We can use this to carry out further analysis,
# or just print it out for confirmation of the results.
print(results)
