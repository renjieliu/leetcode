class Solution:
    def minimumDifference(self, nums: 'List[int]', k: int) -> int:
        nums.sort()
        output = float('inf')
        for i in range(len(nums)-k+1):
            output = min(output, nums[i+k-1] - nums[i])
        return output

