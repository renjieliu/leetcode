class Solution:
    def jump(self, nums: 'List[int]') -> int:
        def helper(dp, arr, pos):
            if dp[pos] != float('inf'):
                return dp[pos]
            elif pos == len(arr)-1:
                return 0
            elif arr[pos] == 0: #cannot move if it's 0
                return float('inf')
            else:
                for i in range(pos+1, min(len(arr),pos+1+arr[pos])) : #from curr location to max it can reach
                    curr = 1+ helper(dp, arr, i)
                    dp[pos] = min(curr, dp[pos])
                return dp[pos]
        if len(nums) == 1 :
            return 0
        dp = [float('inf') for _ in nums]
        helper(dp, nums, 0)
        #print(dp)
        return dp[0]

