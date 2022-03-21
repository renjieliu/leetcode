class Solution:
    def divideArray(self, nums: 'List[int]') -> bool:
        hmp = {}
        for n in nums: # count the occurrence of each element
            if n not in hmp:
                hmp[n] = 0 
            hmp[n] += 1
        for k, v in hmp.items(): # to check if each element appears even number of times.
            if v%2!= 0:
                return False
        return True
    

    
