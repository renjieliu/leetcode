class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> int:
        if nums == []:
            return 0
        else:
            dp = [[1, 1]]
            for i in range(1, len(nums)):
                m = 1  # current length
                repeating = 0  # how many combinations
                for j in range(i):
                    if nums[j] < nums[i]:
                        if dp[j][0] + 1 == m:
                            repeating += dp[j][1]
                        elif dp[j][0] + 1 > m:
                            repeating = dp[j][1]
                            m = dp[j][0] + 1
                dp.append([m, max(1, repeating)])
        hmp = {}
        for i in dp:
            if i[0] not in hmp:
                hmp[i[0]] = 0
            hmp[i[0]] += i[1]

        # print(dp, hmp)
        k = sorted(list(hmp.keys()), reverse=True)[0]
        return hmp[k]










