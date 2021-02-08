class Solution:
    def combinationSum4(self, nums: 'List[int]', target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # current number is "target"
        for i in range(1,
                       target + 1):  # calculate from 1 to target --let's assume each one is target. how many ways to get "current target"
            for n in nums:
                if i - n >= 0:  # how many ways to generat i-n
                    dp[i] += dp[i - n]
        return dp[-1]

