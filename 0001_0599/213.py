class Solution:
    def rob(self, nums: 'List[int]') -> int:
        def helper(arr, i, dp):
            if dp[i] != -1:
                return dp[i]
            if len(arr[i:]) == 0:
                dp[i] = 0
                return dp[i]
            elif len(arr[i:]) <= 2:
                dp[i] = max(arr[i:])
                return dp[i]
            else:
                a = arr[i] + helper(arr, i + 2, dp)
                b = arr[i + 1] + helper(arr, i + 3, dp)
                dp[i] = max(a, b)
                return dp[i]

        if len(nums) <= 2:
            return max(nums)
        dp = [-1] * len(nums)
        helper(nums[:-1], 0, dp)  # pick the first one, and the last one cannot be picked
        output_1 = max(dp)
        dp = [-1] * len(nums)
        helper(nums[1:], 0, dp)  # pick the last one, and the first one cannot be picked
        output_2 = max(dp)
        return max(output_1, output_2)

