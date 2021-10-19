class Solution:
    def minPairSum(self, nums: 'List[int]') -> int:
        nums.sort()
        i = 0
        output = -float('inf')
        while i < len(nums)//2:
            output = max(output, nums[i] + nums[-(i+1)] )
            i+=1
        return output

