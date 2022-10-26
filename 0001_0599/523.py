class Solution:
    def checkSubarraySum(self, nums: 'List[int]', k: int) -> bool:  # O( N | N )
        prefix = {0: -1} # {mod, location} 
        s = 0
        for i, n in enumerate(nums):
            s += n
            if s % k not in prefix:
                prefix[s%k] = i
            elif i - prefix[s%k] > 1: # mod value was seen before, the gap is multiples of k, it needs to have more than 1 elements
                return True
        return False 

    

