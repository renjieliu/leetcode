class Solution:
    def subArrayRanges(self, nums: 'List[int]') -> int:
        output = 0 
        for i in range(len(nums)):
            mi = nums[i]
            mx = nums[i]
            for j in range(i+1, len(nums)): # expand the subarray to here, and check if current number is the max or min
                mi = min(nums[j], mi)
                mx = max(nums[j], mx)
                output += mx-mi
        return output


    
