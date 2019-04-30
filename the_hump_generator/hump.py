#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create time series according to the difference equation: y[i+1] = beta * y[i] * (1 - y[i])
Either as an array or as a generator.
"""

import numpy


def series(n, y0, beta):
    """
    Get a time series as an array.
    
    Arguments:
    n    -- int number of time steps
    y0   -- float starting value of y at time 0 (suggested values between 0. and 1.)
    beta -- float tuning parameter governing the form of the time series (suggested values between 0. and 4.)
    
    Returns:
    1D numpy array of float y values
    """
    y = numpy.full(n, 0.)
    y[0] = y0
    for i in range(1, n):
        y[i] = beta * y[i-1] * (1 - y[i-1])
    return y


def generate(n, y0, beta):
    """
    Get a time series as a generator.
    
    Arguments:
    n    -- int number of time steps
    y0   -- float starting value of y at time 0 (suggested values between 0. and 1.)
    beta -- float tuning parameter governing the form of the time series (suggested values between 0. and 4.)
    
    Returns:
    generator object yielding successive float y values in the series
    """
    y = y0
    for i in range(n):
        yield y
        y = beta * y * (1 - y)
