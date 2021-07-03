class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        output = nums[0]
        curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            output = max(output, curr)
        return output

