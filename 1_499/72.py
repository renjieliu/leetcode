class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for r in range(len(word1)+1):
            dp.append([r])
            for c in range(1, len(word2)+1): # dp has one more column than the word.
                if r==0:
                    dp[-1].append(dp[-1][-1]+1) # as if the other one is blank, for the first row.
                elif r > 0:
                    cost = 0 if word1[r-1] == word2[c-1] else 1
                    dp[-1].append( min(dp[-1][-1]+1, dp[-2][c] +1, dp[-2][c-1] + cost)) # [add, del, replace ]
        return dp[-1][-1]