class Solution:
    def maxAscendingSum(self, nums: 'List[int]') -> int:
        output = curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr = nums[i]
                output = max(output, curr)
            else:
                curr += nums[i]
                output = max(output, curr)
        return output
