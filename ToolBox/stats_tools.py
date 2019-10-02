class Stats:
    """ A class containing util functions for stats. """
    def __init__(self, data):
        self.data = data
    
    def mean(self):
        return sum(self.data)/len(self.data)
    
    def mode(self):
        return max(self.data, key=self.data.count)
    
    def median(self):
        # Finds the median of a pre-sorted list
        def premedian(l):
          if len(l) == 0:
            raise ValueError('Input must be a non-empty list.')
          elif len(l) == 1:
            return l[0]
          elif len(l) == 2:
            return sum(l)/2
          else: return premedian(l[1:-1])

        return premedian(sorted(self.data))
    
    def var(self):
        return sum(list(map(lambda x: (x-self.mean())**2, self.data)))/(len(self.data)-1)
    
    def std(self):
        return self.var()**(1/2)
    
    def coef_of_var(self):
        return self.std()/self.mean()

    