class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool: # O( N | 1 )
        for i in range(num+1): # try all the numbers, and see if it can satisfy the requirement 
            if int(str(i)[::-1]) + i == num:
                return True 
        return False

    
