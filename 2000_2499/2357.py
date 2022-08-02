class Solution:
    def minimumOperations(self, nums: 'List[int]') -> int: #O(N | N)
        return len(set([_ for _ in nums if _])) # Return the distinct count of number > 0
    
