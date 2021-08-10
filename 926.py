class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = [0] * len(s) # one count before
        zero = [0] * len(s) # zero count after
        for i in range(1, len(s)):
            one[i] = one[i-1] + (1 if s[i-1] == "1" else 0)
        for i in range(len(s)-2,-1, -1 ):
            zero[i] = zero[i+1] + (1 if s[i+1] == "0" else 0)
        output = min(zero[0], one[-1])
        for i, c in enumerate(s):
            if c == "1":
                output = min(output, zero[i]+one[i]) #change prev 1 to 0 or change remaining 0 to 1
        return output


# previous approach
# class Solution:
#     def minFlipsMonoIncr(self, s: str) -> int:
#         one = 0
#         zero = 0
#         dp = []
#         for i in s:
#             dp.append([one, 0]) #how many 1 before curr
#             if i == "1":
#                 one += 1
#             else:
#                 zero += 1
#         output = min(one, zero)
#         zero = 0
#         for i in range(len(s)-1, -1, -1): # how many 0's after curr
#             dp[i][1] = zero
#             zero += 1 if s[i] == "0" else 0
#
#         for i, c in enumerate(s):
#             if c == "1":
#                 output = min(output, dp[i][0]+dp[i][1]) #change prev 1's to 0 and after 0's to 1
#         return output


# previous approach
# class Solution:
#     def minFlipsMonoIncr(self, S: str) -> int:
#         one = 0
#         zero = 0
#         dp = []
#         for i in S:
#             dp.append([one, 0])
#             if i == '1':
#                 one += 1  # how many ones before curr
#             else:
#                 zero += 1  # just to count how many zeroes are in the string.
#
#         output = min(one, zero)  # to change every thing to 1 or 0
#         zero = 0  # count 0 after curr
#         for i in range(len(S) - 1, -1, -1):
#             dp[i][1] = zero  # how many 0 after curr
#             if S[i] == '0':
#                 zero += 1
#
#         for i in range(
#                 len(S)):  # flip all the previous 0 to 1 , and following 1 to 0, make it in the format as 00001111
#             if S[i] == '1':
#                 output = min(output, dp[i][0] + dp[i][1])
#
#         return output




