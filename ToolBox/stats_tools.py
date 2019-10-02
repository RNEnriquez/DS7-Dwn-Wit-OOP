import numpy

class Stats:
    def __init__(self,li):
        self.li = li


    def mean(self):
        getmean = sum(self.li) / len(self.li)
        return(getmean)


    def mode(self):
        most = max(list(map(self.li.count, self.li)))
        return list(set(filter(lambda x: self.li.count(x) == most, self.li)))

    def median(self):
        sortedLst = sorted(self.li)
        lstLen = len(self.li)
        index = (lstLen - 1) // 2

        if (lstLen % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1])/2.0
