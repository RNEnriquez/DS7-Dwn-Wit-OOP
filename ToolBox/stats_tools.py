class Stats():
    vector = []

    def __init__(self, vector):
        self.vector = vector
        assert type(self.vector) == type([])
    
    def mean(self):
        assert len(self.vector) > 0
        return sum(self.vector) / len(self.vector)

    def median(self):
        sv  = sorted(self.vector)
        mid_idx = (len(self.vector)  - 1) // 2


        if len(self.vector) % 2 == 1:
            return sv[mid_idx]
        else:
            return (sv[mid_idx] + sv[mid_idx + 1]) / 2.0
    
    def mode(self):
        set_v = set(self.vector)
        current_mode = 0
        for i,x in enumerate(set_v):
            current_mode_count = self.vector.count( self.vector[current_mode])
            if self.vector.count(x) > current_mode_count:
                current_mode = i
        
        return self.vector[current_mode]
    
    def variance(self):
        assert len(self.vector) > 0
        _mean = self.mean()
        return sum([(x - _mean) ** 2 for x in self.vector]) / len(self.vector)
    
    def std(self):
        return self.variance() ** 0.5
    
    def coef_variation(self):
        return self.std() / self.mean()


import numpy as np
def TestStats():
    stats = Stats([1,2,3,4,5])
    assert stats.mean() == np.mean(stats.vector)
    assert stats.median() == np.median(stats.vector)
    assert stats.variance() == np.var(stats.vector)
    assert stats.std() == np.std(stats.vector)
    assert stats.coef_variation() == (np.std(stats.vector) / np.mean(stats.vector))
