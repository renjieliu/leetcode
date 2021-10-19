class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> int: #O(n)
        lkp = set(nums)
        if len(lkp) <= 1:
            return len(lkp)

        def dfs(dp, lkp, n):  # check each number, to find the smaller one.. if cannot find, then return 1
            dp[n] = 1
            if n - 1 in lkp:
                if n - 1 in dp:
                    dp[n] += dp[n - 1]
                else:
                    dp[n] += dfs(dp, lkp, n - 1)  # how many consecutive number it can find
            return dp[n]

        dp = {}
        for n in lkp:  # check each number, and each number is calculated once.
            if n not in dp:
                dfs(dp, lkp, n)
        return max(dp.values())

# previous approach O(nlogn)
# class Solution:
#     def longestConsecutive(self, nums: 'List[int]') -> int:
#         nums = list(set(nums))
#         if len(nums) <= 1: return len(nums)
#         output = 1
#         cnt = 1
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] - nums[i-1] == 1:
#                 cnt += 1
#             else:
#                 cnt = 1
#             output = max(output, cnt)
#         return output
#

