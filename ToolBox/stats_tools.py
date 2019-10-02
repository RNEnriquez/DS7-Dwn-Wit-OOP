class Stats:
    """ A class containing util functions for stats. """
    def __init__(self, data):
        self.data = list(data)
        self.len = len(self.data)
        self.sum = sum(self.data)
        self.sorted = sorted(self.data)

    def mean(self):
        return self.sum/self.len

    def mode(self):
        return max(self.data, key=self.data.count)

    def median(self):
        if self.len % 2 == 0:
            return sum(self.sorted[self.len//2-1:self.len//2+1])/2
        else:
            return self.sorted[self.len//2]

    def var(self):
        return sum(list(map(lambda x: (x-self.mean())**2, self.data)))/(self.len-1)

    def std(self):
        return self.var()**(1/2)

    def coef_of_var(self):
        return self.std()/self.mean()

