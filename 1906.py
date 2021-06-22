class Solution:
    def minDifference(self, nums: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        m = max(nums)
        dp = [[0 for c in range(m+1)]]  #add one more line for the 0 line, to make comparison easier
        for i, c in enumerate(nums):
            dp.append(dp[-1][:])
            dp[-1][c] += 1
        output = []
        for s, e in queries: # to check the changes happened in between. and see what's the most adjacent number appeared
            arr = []
            for i in range(m+1):
                if dp[s][i] != dp[e+1][i]: #check the s-1 line and current. there are len(nums) + 1 lines in the dp
                    arr.append(i)
            if len(arr) < 2:
                output.append(-1)
            else:
                curr = float('inf')
                for i in range(1, len(arr)):
                    curr = min(curr, arr[i] - arr[i-1])
                output.append(curr)
        return output

