#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to produce a rose-tinted version of an image.
"""

import webbrowser
import imageio
import matplotlib.pyplot as plt


# The imageio module provides functions for reading and writing image files.
# (In computing, 'io' stands for input/output,
# and refers to reading and writing to and from various things,
# most commonly files on the hard disk of the computer.)

# The imread() function reads in an image file.
# We use it here to read the example image.
filename = 'example.jpg'
img = imageio.imread(filename)

# The result is an array of numbers.
# This array represents the colors of the pixels in the image.
# The shape attribute of the image array tells us its dimensions.
# The convention in Python is rows first, then columns, then 'layers'.
# The layers of the array represent its colors,
# in three 'channels': red, green, and blue.
height, width, nChannels = img.shape

# Print out confirmation of the image's characteristics.
msg = '{}: {}x{} pixels, {} color channels'.format(filename, width, height, nChannels)
print(msg)


# The pyplot module from matplotlib provides plotting functions.
# The syntax of the functions is based on Matlab's plotting functions,
# so as you can imagine it is pretty spectacularly awful.
# But it is a widespread standard and can do lots of useful things.

# Here we just use matplotlib's imshow() function to plot the image we loaded,
# so that we can confirm that it has loaded correctly.
# The show() function ensures that the plot is displayed.
plt.imshow(img)
plt.show()


# A rose (or pink) color is made of red and white,
# as we learned from mixing paints at school.
# The red part of the tint is easy to achieve.
# For this we just need to set the red channel of the image to maximum.
# The color values can range from 0 to 255.
img[:, :, 0] = 255

# White is made of all the colors together,
# as we learned in physics class by means of some demonstration I forget.
# So to get the white part of the tint we need to increase all color channels.
# In practice this means increasing the blue and green channels,
# since we have already increased the red channel to maximum.
# We shouldn't increase blue and green too much or the image will just be white.
# So we increase them by half the distance between the current value and the maximum.
img[:, :, 1:] = img[:, :, 1:] + 0.5 * (255 - img[:, :, 1:])

# Check the result.
plt.imshow(img)
plt.show()


# We can also write the altered image to a new file.
newFilename = 'tinted_' + filename
imageio.imwrite(newFilename, img)

# And then open the resulting file outside of Python.
webbrowser.open(newFilename)
