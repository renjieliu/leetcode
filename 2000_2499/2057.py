class Solution:
    def smallestEqual(self, nums: 'List[int]') -> int:
        for i, n in enumerate(nums):
            if n==i%10:
                return i
        return -1

    
