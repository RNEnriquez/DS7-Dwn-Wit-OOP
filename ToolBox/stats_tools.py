"""
stats functions for mean, median, mode, 
variance, standard deviation, and coefficient of variation
"""

import numpy as np


class Stats:

    def __init__(self, data):
        self.data = list(data)
        self.size = len(data)

    def mean(self):
        """
        function to calculate mean of data
        """
        mean = sum(self.data)/self.size
        return mean
    
    def median(self):
        """
        function to calculate median of data
        """
        self.data.sort()

        if len(self.data) % 2 == 1:
            median = self.data[int(self.size/2)]
        else:
            median = (self.data[int(self.size/2 - 1)] + 
                    self.data[int(self.size/2)]) / 2
        return median
    
    def mode(self):
        """
        function to get mode of data, only returns the first it encounters if
        there are more than 1 mode
        """
        mode = max(self.data, key=self.data.count)
        return mode

    def variance(self, sample=True):
        """
        function to calculate variance of data

        by default, it calculates sample variance, change sample=False if you
        want to calculate population.
        """
        distance_squared = list(map(lambda x: (x - sum(self.data)/self.size)**2, self.data))

        if sample == True:
            variance = sum(distance_squared)/(self.size - 1)
        if sample == False: 
            variance = sum(distance_squared)/(self.size)
        return variance

    def stddev(self, sample=True):
        """
        function to calculate standard deviation of data

        by default, it calculates sample standard deviation, change
        sample=False if you want to calculate population.
        """
        distance_squared = list(map(lambda x: (x - sum(self.data)/self.size)**2, self.data))

        if sample == True:
            variance = sum(distance_squared)/(self.size - 1)
            stddev = variance**(1/2)
        if sample == False:
            variance = sum(distance_squared)/(self.size)
            stddev = variance**(1/2)
        return stddev 

    def coeffvar(self, sample=True):
        """
        function to calculate the coefficient of variance of data

        by default, it calculates sample coefficient of variance, change
        sample=False if you want to calculate population.
        """
        mean = sum(self.data)/self.size
        distance_squared = list(map(lambda x: (x - sum(self.data)/self.size)**2, self.data))

        if sample == True:
            variance = sum(distance_squared)/(self.size - 1)
            stddev = variance**(1/2)
            coeffvar = stddev/mean
        if sample == False:
            variance = sum(distance_squared)/(self.size)
            stddev = variance**(1/2)
            coeffvar = stddev/mean
        return coeffvar
