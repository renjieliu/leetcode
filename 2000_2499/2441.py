class Solution:
    def findMaxK(self, nums: 'List[int]') -> int: # O( N | N )
        output = -1 # default the output to -1
        lkp = set(nums)
        for n in lkp:
            if n > 0 and -n in lkp: # n needs to be positive, and -n is also in the lookup set
                output = max(output, n)
        return output 
    

