class Solution:
    def triangularSum(self, nums: 'List[int]') -> int:
        while len(nums) > 1: #using the same structure as BFS, to eliminate the nums until only 1 element left
            nxt =[]
            for i in range(1, len(nums)):
                nxt.append((nums[i] + nums[i-1])%10)
            nums = nxt 
        return nums[0]
    
    

            
