class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured ==0:
            dp = [[[0,0]]] #[current, remaining]
        else:
            dp = [[[1, poured-1]]]
        if query_row == 0:
            return dp[0][0][0] # [row, element, curr]
        else:
            for i in range(1, query_row+1):
                dp.append([])
                for j in range(i+1): #add for each cup
                    if j == 0: # rem = prevrem -1
                        suppose = dp[-2][0][1]/2
                        curr = 1 if suppose >= 1 else suppose # prevRem / 2 
                        rem = 0 if suppose<=1 else suppose-1
                        dp[-1].append([curr, rem])
                    elif j == i:
                        suppose = dp[-2][-1][1]/2
                        curr = 1 if suppose >= 1 else suppose # prevRem / 2 
                        rem = 0 if suppose<=1 else suppose-1
                        dp[-1].append([curr, rem])
                    else: 
                        left = dp[-2][j-1][1]/2
                        right = dp[-2][j][1]/2
                        suppose = left + right
                        curr = 1 if suppose >= 1 else suppose # prevRem / 2 
                        rem = 0 if suppose<=1 else suppose-1
                        dp[-1].append([curr, rem])
            #print(dp)            
            return dp[-1][query_glass][0]