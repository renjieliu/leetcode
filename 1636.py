class Solution:
    def frequencySort(self, nums: 'List[int]') -> 'List[int]':
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] +=1
        arr = [[k,v] for k, v in hmp.items()]
        arr.sort(key = lambda x: x[0], reverse = True)
        arr.sort(key = lambda x:x[1])
        output = []
        for a, b in arr:
            output += [a] * b
        return output