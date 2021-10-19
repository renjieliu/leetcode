class Solution:
    def minMoves2(self, nums: 'List[int]') -> int:
        nums.sort()
        medium = nums[len(nums)//2]
        return sum([abs(n-medium) for n in nums])

