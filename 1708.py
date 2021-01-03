class Solution:
    def largestSubarray(self, nums: 'List[int]', k: int) -> 'List[int]':
        idx = -1
        maxx = -float('inf')
        for i in range(len(nums) - k, -1, -1):
            if nums[i] > maxx:
                maxx = nums[i]
                idx = i
        return nums[idx: idx + k]
