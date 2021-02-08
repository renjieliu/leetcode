class Solution:
    def findMin(self, nums: 'List[int]') -> int:
        for n in nums:  # O(n)
            if n < nums[0]:
                return n
        return nums[0]
