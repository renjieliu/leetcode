class Solution:
    def findClosestNumber(self, nums: 'List[int]') -> int: #O(N | 1)
        output = -float('inf') 
        diff = float('inf') 
        for n in nums:
            if abs(n) <= diff: #check the distance from 0
                if abs(n) == diff:
                    output = max(output, n)
                    diff = abs(n)
                else:
                    diff = abs(n)  
                    output = n
        return output
    

    
