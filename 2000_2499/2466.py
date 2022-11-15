class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int: # O( N | N )
        mod = 10**9+7
        dp = [1] # one way to form 0-length.
        for i in range(1, high+2):
            A = B = 0 
            if i - zero >= 0: # previous ways to form zero
                A = dp[i-zero]
            if i - one >= 0 : # previous ways to form one
                B = dp[i-one]
            dp.append(A+B)
        
        return sum(dp[low:high+1])%mod # total from low to high, and mod per requirement


