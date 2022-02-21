class Solution:
    def countPairs(self, nums: 'List[int]', k: int) -> int: #O(N2)
        cnt = 0 
        for i in range(len(nums)): #go through each number, and see if it can meet the condition
            for j in range(i+1, len(nums)):
                cnt+= 1 if nums[i] == nums[j] and i*j%k == 0 else 0
        return cnt
    
    
    
