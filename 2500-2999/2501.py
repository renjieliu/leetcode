class Solution:
    def longestSquareStreak(self, nums: 'List[int]') -> int: # O( N | N )
        lkp = set(nums) 
        cnt = {} #record how many **2 can be found from current number
        def dfs(cnt, lkp, curr):
            if curr not in lkp:
                return 0
            if curr not in cnt:
                cnt[curr] = 1 + dfs(cnt, lkp, curr**2) # from curr, check the following
            return cnt[curr]
        
        for n in lkp:
            dfs(cnt, lkp, n)
        
        output = max(cnt.values())
        return -1 if output <= 1 else output

    
