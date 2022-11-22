class Solution:
    def unequalTriplets(self, nums: 'List[int]') -> int: # O( N**3 | 1 )
        cnt = 0 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    cnt += 1  if nums[i] != nums[j] != nums[k] and nums[i] != nums[k] else 0 
        return cnt
    


