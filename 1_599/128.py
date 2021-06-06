class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> int:
        nums = list(set(nums))
        if len(nums) <= 1: return len(nums)
        output = 1
        cnt = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cnt += 1
            else:
                cnt = 1
            output = max(output, cnt)
        return output


