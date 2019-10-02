import numpy
import math
class Stats:

    def __init__(self, list_var):
        self.list_var = list_var
    
    def mean_form(self):
        sum_total = sum(self.list_var)
        average = sum_total/len(self.list_var)
        return average
    
    def median_form(self):
        length_list = len(self.list_var)

        if length_list % 2 == 0:
            even = ((length_list / 2) + ((length_list + 2) / 2)) / 2
            return even
        else:
            odd = (length_list + 1) / 2
            return odd
    
    def variance_form(self):
        result = (sum((xi - mean_form(self.list_var)) ** 2 for xi in self.list_var) / len(self.list_var))
        return result
    
    def std_deviation(self):
        result = math.sqrt(variance_form(self.list_var))
        return result
    