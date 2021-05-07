class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        for r in range(len(word2)+1):
            dp.append([])
            for c in range(len(word1)+1):
                if r==0: #first row should be 0,1,2,3
                    dp[-1].append(c)
                elif c == 0: #first col should be 0,1,2,3
                    dp[-1].append(r)
                else: #if same, then use the r-1,c-1,
                    if word2[r-1] == word1[c-1]:
                        dp[-1].append(dp[-2][c-1])
                    else:#[r-1][c-1]+2: delete both, or ([r-1][c], [r][c-1]) +1: delete one of them
                        dp[-1].append(min(dp[-2][c-1]+2, dp[-2][c]+1, dp[-1][c-1]+1))
        return dp[-1][-1]
