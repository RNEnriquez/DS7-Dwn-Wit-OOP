class Stats:
    def mean(dict):

        total_dict= reduce((lambda x,y: x+y),dict)
        mean = total_dict/len(dict)
  
        return mean

     def median(dict):

        n = len(dict)
        dict.sort()
        if n % 2 == 0:
        median1 = dict[n//2] 
        median2 = dict[n//2 - 1] 
        median = (median1 + median2)/2
        else:
        median = dict[n//2] 
    
        return median

      def mode(dict):

         mode = None
         mapping = {x: 0 for x in dict}
         greatestFrequency = 0
         for n in dict:
         mapping[n] += 1
         if mapping[n] > greatestFrequency:
         greatestFrequency = mapping[n]
         mode = n
         return mode
