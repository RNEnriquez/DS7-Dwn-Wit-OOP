

class Stats:
    """ Class of basic statistics methods implemented without numpy. """
    def __init__(self, numbers):
        self.numbers=numbers

    def mean(self):
        return sum(self.numbers)/len(self.numbers)

    def median(self):
        """ Calculates median by first finding the midpoint depending on
            whether the self.numbers is even- or odd-length. """
        if len(self.numbers) % 2 == 0:
            halfway = len(self.numbers) / 2
            return sum(sorted(self.numbers)[int(halfway) - 1 : int(halfway) + 1]) / 2
        else:
            halfway = len(self.numbers) // 2
            return sorted(self.numbers)[halfway]

    def mode(self):
        highest = 0
        mode = 0
        no_mode = True
        for i in set(self.numbers):
            counted = self.numbers.count(i)
            if counted > highest:
                highest = counted
                mode = i
                no_mode = False
            elif counted == highest and i != mode:
                no_mode = True
        if no_mode == False:
            return mode
        elif no_mode == True:
            return None

    def variance(self):
        sample_mean = self.mean()
        squared_deviations = []
        for i in self.numbers:
            deviation = i - sample_mean
            squared_deviations.append(deviation**2)
        sse = sum(squared_deviations)
        return sse / (len(self.numbers) - 1)

    def std(self):
        return self.variance()**0.5

    def coef_var(self):
        return self.std() / self.mean()
