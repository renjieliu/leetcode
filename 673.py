class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> int:
        if nums == []:
            return 0
        else:
            dp = [[1, 1]]  # [longest, combinations]
            for i in range(1, len(nums)):
                currLength = 1
                combinations = 1
                for j in range(i - 1, -1, -1):
                    if nums[j] < nums[i]:
                        if dp[j][0] + 1 == currLength:
                            combinations += dp[j][1]
                        if dp[j][0] + 1 > currLength:
                            combinations = dp[j][1]
                            currLength = dp[j][0] + 1
                dp.append([currLength, combinations])

            l = max([l for l, c in dp])  # find the max length
            output = sum([b for a, b in dp if a == l])  # sum how many combinations
            return output

