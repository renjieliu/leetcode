class Solution:
    def numDecodings(self, s: str) -> int: # O( N | N )
        def helper(hmp, s): #store the current s in the hmp, to avoid double counting
            if s in hmp:
                return hmp[s]
            else:
                hmp[s] = 0 
                if s and s[0] != "0":
                    if len(s) == 1:
                        hmp[s] = 1
                    else:
                        if int(s[:2])<=26:
                            if s[1] == "0": # take the first 2 characters as a whole
                                hmp[s] = helper(hmp, s[2:])
                            else:
                                A = helper(hmp, s[1:])
                                B = helper(hmp, s[2:])
                                hmp[s] = A + B
                        else:
                            hmp[s] = helper(hmp, s[1:])
                # print(hmp)
                return hmp[s]

        return helper({"": 1}, s) #if the string can be used as a whole - "" remaining, it's 1 way to decode.
                        
                            
                

                




# previous solution

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         def helper(dp, s, loc):
#             if loc in dp:
#                 return dp[loc]
#             else:
#                 if loc >= len(s):
#                     dp[loc] = 1
#                 elif len(s[loc:]) == 1:
#                     dp[loc] = 0 if s[loc:] == "0" else 1
#                 else:
#                     if s[loc] == "0": #cannot start the number with 0
#                         dp[loc] = 0
#                     elif int(s[loc:loc+2]) <= 26:
#                         if s[loc+1] == "0": #for 10, 20, need to take first 2 character
#                             dp[loc] = helper(dp, s, loc+2)
#                         else:
#                             A = helper(dp, s, loc+1) #take away first number, calc the rest
#                             B = helper(dp, s, loc+2) #take away first two numbers, calc the rest
#                             dp[loc] = A + B
#                     else:
#                         dp[loc] = helper(dp, s, loc+1)
#                 return dp[loc]

#         dp = {}
#         helper(dp, s, 0)
#         #print(dp)
#         return dp[0] # if 0 not in dp.values() else 0



# previous approach
# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not s:
#             return 0
#
#         # Array to store the subproblem results
#         dp = [0 for _ in range(len(s) + 1)]
#
#         dp[0] = 1
#         # Ways to decode a string of size 1 is 1. Unless the string is '0'.
#         # '0' doesn't have a single digit decode.
#         dp[1] = 0 if s[0] == '0' else 1
#
#
#         for i in range(2, len(dp)):
#
#             # Check if successful single digit decode is possible.
#             if s[i-1] != '0':
#                 dp[i] += dp[i-1]
#
#             # Check if successful two digit decode is possible.
#             two_digit = int(s[i-2 : i])
#             if two_digit >= 10 and two_digit <= 26:
#                 dp[i] += dp[i-2]
#         return dp[len(s)]