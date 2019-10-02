import numpy as np
import pandas as pd
from collections import Counter

class Stats():
    def __init__(self, list_in=[0, 1, 2, 3, 4]):
        self.list_in = pd.DataFrame(list_in)

    def mean(list_in):
        return (list_in.sum() / len(list_in))

    def median(list_in):
        list_in.sort()
        if len(list_in) % 2 == 0:
            return (list_in[(len(list_in)//2)]+list_in[(len(list_in)//2)-1])/2
        else:
            return list_in[len(list_in)//2]

    def mode(list_in):
        data = Counter(list_in) 
        getMode = dict(data) 
        mode = [k for k, v in getMode.items() if v == max(list(data.values()))]
        if len(mode) == len(num):
            return 'No mode found.'
        else:
            return mode