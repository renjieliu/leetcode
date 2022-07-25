class Solution:
    def zeroFilledSubarray(self, nums: 'List[int]') -> int: # O( N | 1 )
        gauss = lambda x: (1+x)*x//2 #gauss from 1 to x
        total = 0
        r = 0 
        while r < len(nums):
            if nums[r] == 0:
                l = r
                while r < len(nums) and nums[r] == 0: # find all the 0's in current segment, calculate number of subarray, 1+2+3+4... r-l
                    r += 1
                total += gauss(r-l)
            r += 1 
        return total
    

            
