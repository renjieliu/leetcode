class Solution:
    def findFinalValue(self, nums: 'List[int]', original: int) -> int:
        nums = set(nums) 
        while original in nums:
            original <<= 1 # same as original * 2
        return original
    
