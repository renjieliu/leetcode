class Solution:
    def longestSubarray(self, nums: 'List[int]') -> int: # O( N | 1 )
        m = max(nums) # the max number & other number will become smaller.  
        output = 1
        curr = 1
        for i in range(1,len(nums)): # to find the continuous array with the max number
            if nums[i] == nums[i-1] == m: #same as the m and continous
                curr += 1 
            else: #otherwise, reset the curr
                curr = 1
            output = max(output, curr)
        
        return output

    
