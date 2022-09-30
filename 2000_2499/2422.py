class Solution:
    def minimumOperations(self, nums: 'List[int]') -> int: # O( N | 1 )
        l = 0
        r = len(nums)-1
        cnt = 0 
        left = 0 #current total from left 
        right = 0  #current total from right
        
        while l < r:
            left = nums[l]
            right = nums[r]
            while l < r and left != right: #keep adding the left or right until they are same
                if left < right:
                    l += 1
                    left += nums[l]
                    cnt += 1
                else:
                    r -= 1 
                    right += nums[r]
                    cnt += 1
            l += 1 
            r -= 1
            
        return cnt
          
