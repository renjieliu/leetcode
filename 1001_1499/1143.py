class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: # O( MN | N ) M = len(text1), N = len(text2)
        dp = [0 for c in range(len(text2)+1)]
        for r in range(len(text1)):
            arr = [0]
            for c in range(len(text2)):
                if text1[r] == text2[c]:
                    arr.append(dp[c] + 1) #prevRow_prevCol + 1 
                else:
                    arr.append(max(arr[c], dp[c+1])) #sameRow_prevCol + 1 or prevRow_sameCol+1
            dp = arr
        return dp[-1]
                    
        


# previous solution

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
#         def helper(s1, s2, i, j,dp):
#             if dp[i][j] != None:
#                 return dp[i][j]
#             elif len(s1)*len(s2) == 0:
#                 dp[i][j] = 0
#                 return dp[i][j]
#             else:
#                 if s1[-1] == s2[-1]:
#                     dp[i][j] = 1+helper(s1[:-1], s2[:-1], i-1, j-1, dp)
#                 else:
#                     dp[i][j] = max(helper(s1[:-1], s2, i-1, j, dp), helper(s1, s2[:-1], i, j-1, dp))
#                 return dp[i][j] 
        
#         dp = [[None for _ in range(len(text2)+1)] for _ in range (len(text1)+1)]
#         helper(text1, text2, len(text1), len(text2), dp)
#         #print(dp)
#         return dp[-1][-1]
            
        

            
        
        



# previous solution

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
#         def helper(s1, s2, i, j,dp):
#             if dp[i][j] != None:
#                 return dp[i][j]
#             elif len(s1)*len(s2) == 0:
#                 dp[i][j] = 0
#                 return dp[i][j]
#             else:
#                 if s1[-1] == s2[-1]:
#                     dp[i][j] = 1+helper(s1[:-1], s2[:-1], i-1, j-1, dp)
#                 else:
#                     dp[i][j] = max(helper(s1[:-1], s2, i-1, j, dp), helper(s1, s2[:-1], i, j-1, dp))
#                 return dp[i][j] 
        
#         dp = [[None for _ in range(len(text2)+1)] for _ in range (len(text1)+1)]
#         helper(text1, text2, len(text1), len(text2), dp)
#         #print(dp)
#         return dp[-1][-1]
            
        



# previous solution

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def dp(t1, t2, i , j,  dict):
#             if len(t1) <=0 or len(t2) <= 0:
#                 return 0

#             elif dict[i][j] != -1 :
#                 return dict[i][j]

#             else:
#                 if t1[-1] == t2[-1]:
#                     return 1 + dp(t1[:-1], t2[:-1], i-1, j-1, dict)
#                 else:
#                     #print(dp(t1, t2[:-1], i, j-1, dict), dp(t1[:-1], t2, i-1, j , dict))
#                     dict[i][j] = max(dp(t1, t2[:-1], i, j-1, dict), dp(t1[:-1], t2, i-1, j , dict))
#                     return dict[i][j]

#         return dp(text1, text2, len(text1)-1, len(text2)-1,  [[-1 for _ in range(len(text2))] for _ in range(len(text1)) ] )







# previous solution

# class Solution:
#     def longestCommonSubsequence(text1: str, text2: str) -> int:
#         dp = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
#         # when start comparing, it's comparing with the "", so the first column and the first row of the matrix should all be 0

#         # for r in range(len(dp)):
#         #     if r == 0:
#         #         for c in range(len(dp[0])):
#         #             dp[r][c] =0
#         #     dp[r][0] = 0
#         # dp matrix has len(text1)+1 cols and len(text2)+1 rows
#         for r in range(len(text2)):
#             for c in range(len(text1)):
#                 if text2[r] == text1[c]:
#                     if r == 0 or c == 0:
#                         dp[r][c] = 1
#                     else:
#                         dp[r][c] = 1 + dp[r - 1][c - 1]
#                 else:
#                     if r == 0 and c == 0:
#                         dp[r][c] = 0
#                     elif r == 0 and c != 0:
#                         dp[r][c] = dp[0][c - 1]
#                     elif r != 0 and c == 0:
#                         dp[r][c] = dp[r - 1][0]
#                     else:
#                         dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

#         return dp[-1][-1]






