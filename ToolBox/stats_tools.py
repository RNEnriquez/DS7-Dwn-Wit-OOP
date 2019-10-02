class Stats:


    def mean(list):
        return sum(list) / len(list)


    def median(list):
    data.sort()
    if len(list) % 2 != 0:
        idx = int((len(list) - 1) / 2)
        return list[idx]
    else:
        idx_1 = list[int((len(list) / 2))]
        idx_2 = list[int((len(list) / 2) - 1)]
        return (idx_1 + idx_2) / 2


    def mode(list):
        counts = {}
        unique_nums = set(list)
        for digit in unique_nums:
            counts[digit] = list.count(digit)
            if max(counts.values()) == 1:
                print("No Mode exists")
            else:
                for key, value in counts.items():
                    if value == max(counts.values()):
                        return key


    def variance(list):
        data = np.array(list)
        return ((data - mean(data))**2).sum() / len(data)


    def standard_deviation(list):
        return variance(list)**(0.5)


    def coef_var(list):
        return standard_deviation(list) / mean(list)
