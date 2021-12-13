class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def lcm(a, b): # to get the least common multiple
            def gcd(a, b):
                while b :
                    a, b = b, a%b
                return a
            return a*b//(gcd(a, b))
        
        L = lcm(a,b)
        s = 1 
        e = n*a*b
        mod = 10**9+7
        while s <= e: #binary search to find the answer 
            mid = (s+e)//2 
            cnt = mid//a + mid//b - mid//L
            if cnt == n: 
                if mid % a == 0 or mid % b == 0: #if curr is the one, return it  
                    return mid%mod
                else: #the true number is on the left 
                    e = mid - 1  
            elif cnt < n: # not enough
                s = mid + 1
            else: # too large
                e = mid - 1
        
        return s%mod

