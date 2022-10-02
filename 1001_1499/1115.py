class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int: # O( NKT | NKT ) T is target. 
        mod = 10**9+7
        
        def helper(dp, n, k, target):
            if (n, target) in dp:
                return dp[(n, target)] # how many ways when it's n and target
            
            if n == 0 and target == 0: #all are 1
                return 1
            
            if n * k < target or target < 0:
                return 0
           
            dp[(n, target)] = 0
            
            for i in range(1, k+1): # keep finding the previous count
                dp[(n, target)] += helper(dp, n-1, k, target-i)
            return dp[(n, target)]

        return helper({}, n, k, target) % mod
    
    

