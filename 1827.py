class Solution:
    def minOperations(self, nums: 'List[int]') -> int:
        cnt = 0
        for i in range(1,len(nums)):
            curr = nums[i]
            nums[i] = nums[i] if nums[i] > nums[i-1] else nums[i-1]+1
            cnt += nums[i] - curr
        return cnt
