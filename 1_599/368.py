class Solution:
    def largestDivisibleSubset(self, nums: 'List[int]') -> 'List[int]':
        if nums == []: return []
        isGood = lambda x, y: True if x % y == 0 or y % x == 0 else False
        nums.sort()
        loc = 0
        maxx = 0
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if isGood(nums[i], nums[j]):
                    if dp[j] + 1 > maxx:
                        maxx = dp[j] + 1
                        loc = i
                    dp[i] = max(dp[i], dp[j] + 1)

        output = [nums[loc]]
        for i in range(loc - 1, -1, -1):
            # print(i, loc, maxx)
            if isGood(nums[loc], nums[i]) and dp[i] == maxx - len(output):
                output.append(nums[i])
        # print(dp)
        return output
