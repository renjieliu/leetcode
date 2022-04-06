class Solution:
    def isConsecutive(self, nums: 'List[int]') -> bool: #O(N | N)
        return set(i for i in range(min(nums), min(nums)+len(nums)))  ==  set(nums)
    
    