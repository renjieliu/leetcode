class Solution:
    def findSubarrays(self, nums: 'List[int]') -> bool: # O( N | N )
        lkp = set()
        for i in range(1, len(nums)): # check sum of all the subarrays with length 2
            if nums[i] + nums[i-1] in lkp:
                return True
            lkp.add(nums[i] + nums[i-1])
        return False 
    

