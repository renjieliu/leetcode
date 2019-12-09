class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        one = 0
        zero = 0
        dp = []
        for i in S:
            dp.append([one, 0])
            if i == '1':
                one += 1  # how many ones before curr
            else:
                zero += 1  # just to count how many zeroes are in the string.

        output = min(one, zero)  # to change every thing to 1 or 0
        zero = 0  # count 0 after curr
        for i in range(len(S) - 1, -1, -1):
            dp[i][1] = zero  # how many 0 after curr
            if S[i] == '0':
                zero += 1

        for i in range(
                len(S)):  # flip all the previous 0 to 1 , and following 1 to 0, make it in the format as 00001111
            if S[i] == '1':
                output = min(output, dp[i][0] + dp[i][1])

        return output




