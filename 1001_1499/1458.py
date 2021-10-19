class Solution:
    def maxDotProduct(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        dp = [[None for _ in range(len(nums2))] for _ in range(len(nums1))]
        for r in range(len(nums1)):
            for c in range(len(nums2)):
                curr = nums1[r] * nums2[c]
                if r == 0:
                    if c == 0:
                        dp[r][c] = curr
                    else:
                        dp[r][c] = max(dp[r][c - 1], curr)
                else:
                    if c == 0:
                        dp[r][c] = max(dp[r - 1][c], curr)
                    else:
                        dp[r][c] = max(curr, dp[r - 1][c - 1] + curr, dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]

