class Solution:
    def minDistance(self, word1: str, word2: str) -> int: # O( MN | MN )
        dp = [[_ for _ in range(len(word2)+1)]]  # assuming the first character of word1 is ""
        for r in range(len(word1)):
            dp.append([r+1]) #assuming need to delete the first character, to initiate the row
            for c in range(len(word2)):
                left = dp[r+1][c]
                up = dp[r][c+1]
                upperleft = dp[r][c]
                if word1[r] == word2[c]:
                    dp[-1].append(upperleft)
                else:
                    dp[-1].append(min(upperleft+2, up+1, left+1)) # delete both, delete from word1, delete from word2
        # print(dp)
        return dp[-1][-1]

    
# previous solution

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         dp = []
#         for r in range(len(word2)+1):
#             dp.append([])
#             for c in range(len(word1)+1):
#                 if r==0: #first row should be 0,1,2,3
#                     dp[-1].append(c)
#                 elif c == 0: #first col should be 0,1,2,3
#                     dp[-1].append(r)
#                 else: #if same, then use the r-1,c-1,
#                     if word2[r-1] == word1[c-1]:
#                         dp[-1].append(dp[-2][c-1])
#                     else:#[r-1][c-1]+2: delete both, or ([r-1][c], [r][c-1]) +1: delete one of them
#                         dp[-1].append(min(dp[-2][c-1]+2, dp[-2][c]+1, dp[-1][c-1]+1))
#         return dp[-1][-1]



