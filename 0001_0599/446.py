class Solution: # RL 20210910: Copied solution
    def numberOfArithmeticSlices(self, nums: 'List[int]') -> int:
        total = 0
        n = len(nums)
        dp = [defaultdict(int) for _ in nums]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += (dp[j][nums[i] - nums[j]] + 1)
            total += sum(dp[i].values())

        return total - (n-1)*n//2



