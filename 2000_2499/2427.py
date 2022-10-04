class Solution:
    def commonFactors(self, a: int, b: int) -> int: # O( N | 1 )
        mi = min(a, b)
        mx = max(a, b) 
        cnt = 0 
        for i in range(1, mi+1): #check number from 1 to c, and see if it's a common factor for a, b
            cnt += ((mi % i) == 0 and (mx % i) == 0)
        return cnt 
    
