"""
Your Stats class should take in a list
Stats class methods include the mean, median (for odd and even N),
mode, variance, standard deviation, and coefficient of variation
You may use NumPy but not for its math methods
"""
import numpy as np
from functools import reduce


class Stats():

    def __init__(self, list):
        self.list = list


    def mean(self):
        self.x = reduce((lambda x, y: x + y), self.list)
        return(self.x/len(self.list))


    def median(self):
        self.sort_num = sorted(self.list)
        self.middlelist = (len(sort_num)//2)

        if len(self.list) % 2 == 0:
            return(sum((self.sort_num[self.middlelist - 1],
                         self.sort_num[self.middlelist]))/2.0)
        else:
            return(self.sort_num[self.middlelist])


    def mode(self):
        return max(set(self.list), key=self.list.count)


    def variance(self,):
        self.mean_r = self.mean()
        return(sum((x - self.mean_r)**2 for x in self.list)/len(self.list))


    def standard_deviation(self):
        self.variance_r = self.variance()
        return np.sqrt(self.variance_r)


    def coefficient_variation(self):
        self.std_r = self.standard_deviation()
        self.mean_r = self.mean()
        return ((self.std_r/self.mean_r)*100)
