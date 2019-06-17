#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scramble an image by shuffling blocks of pixels.
"""

from itertools import chain
import imageio
import numpy


def imscramble(fileName, blockSize=1, fileNameOut=None):
    """
    Save a scrambled version of an image file.
    The scrambled image consists of shuffled squares of a given width.
    
    Required arguments:
    fileName -- path to the image file
    
    Optional keyword arguments:
    blockSize   -- width of the squares to shuffle (in px)
                   defaults to 1 (i.e. scramble all pixels)
    fileNameOut -- path to save scrambled image to
                   defaults to None (no image file is written)
    
    Returns:
    scrambled image as numpy.array
    """
    
    # Subsequent steps are faster with a numpy array than an imageio array.
    img = numpy.array(imageio.imread(fileName))
    
    height, width = img.shape[:2]
    if (height % blockSize) or (width % blockSize):
        msg = 'blockSize {} incompatible with image dimensions {}x{}'
        raise ValueError(msg.format(blockSize, width, height))
    
    # Faster method for single-pixel scrambling.
    if blockSize == 1:
        img = numpy.reshape(img, (height*width, -1))
        numpy.random.shuffle(img)
        img = numpy.reshape(img, (height, width, -1))
    else:
        
        # Cut the image array into blocks.
        nRows = height // blockSize
        nCols = width // blockSize
        img = numpy.array_split(img, nRows, axis=0)
        img = [numpy.array_split(row, nCols, axis=1) for row in img]
        img = numpy.array(list(chain.from_iterable(img)))
        
        # Shuffle the blocks.
        numpy.random.shuffle(img)
        
        # Put the shuffled blocks back together.
        img = numpy.reshape(img, (nRows, nCols, blockSize, blockSize, -1))
        img = [numpy.concatenate(row, axis=1) for row in img]
        img = numpy.concatenate(img, axis=0)
    
    # Write the new image file.
    if fileNameOut:
        imageio.imwrite(fileNameOut, img)
    
    return img


# Test the example if run as a script.
if __name__ == '__main__':
    
    import webbrowser
    
    # Test block-wise scrambling
    imscramble('example.jpg', blockSize=500, fileNameOut='scrambled_example.jpg')
    webbrowser.open('scrambled_example_1.jpg')
    
    # Test single-pixel scrambling.
    imscramble('example.jpg', fileNameOut='scrambled_example_2.jpg')
    webbrowser.open('scrambled_example_2.jpg')
