class Solution:
    def distinctIntegers(self, n: int) -> int: # O( 1 | 1 )
        return n - (n!=1) # if n == 1 then return 0 else return n-1
    
