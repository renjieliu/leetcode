class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        dp = [1] * len(nums)
        ans = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if nums[j] == nums[i]-1:
                        break
            ans = max(ans, dp[i])
        return ans

