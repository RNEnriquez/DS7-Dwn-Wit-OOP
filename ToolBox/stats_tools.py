import numpy as np


class Stats(list):
    def __init__(self,list):
        self.list = list
        self.length = len(list)
        self.mean = sum(list)/self.length
        #If list is even
        if self.length % 2 == 0:
            self.medianEven = median(list)
        else:
            self.medianOdd = median(list)

            self.mode = mode(list)

            #Used to calculate variance and stanadard deviation
            for x in list:
                self.temp = (x - self.mean)**2

        self.variance = temp/(self.length-1)
        self.std_dev = sqrt(temp/self.length)
        self.cof_var = self.std_dev/self.mean
