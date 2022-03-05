class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == query_glass == 0:
            return min(poured, 1) 
        dp = [[poured-1]] #to record how much champagne left from the prev row
        r = 1
        while True:
            dp.append([])
            for c in range(r+1):
                if c == 0:
                    curr = dp[r-1][c]/2 #how much is current cup
                elif c == r:
                    curr = dp[r-1][c-1]/2
                else:
                    curr = dp[r-1][c-1]/2 + dp[r-1][c]/2
                if r == query_row and c==query_glass:
                    return max(0, min(1, curr)) #if curr < 0 then 0 , if > 1 then 1
                else:
                    rem = max(0, curr-1) #how much will be left to the following lines
                    dp[-1].append(rem)

            r+=1
                    
               


# previous approach

# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         if poured ==0:
#             dp = [[[0,0]]] #[current, remaining]
#         else:
#             dp = [[[1, poured-1]]]
#         if query_row == 0:
#             return dp[0][0][0] # [row, element, curr]
#         else:
#             for i in range(1, query_row+1):
#                 dp.append([])
#                 for j in range(i+1): #add for each cup
#                     if j == 0: # rem = prevrem -1
#                         suppose = dp[-2][0][1]/2
#                         curr = 1 if suppose >= 1 else suppose # prevRem / 2 
#                         rem = 0 if suppose<=1 else suppose-1
#                         dp[-1].append([curr, rem])
#                     elif j == i:
#                         suppose = dp[-2][-1][1]/2
#                         curr = 1 if suppose >= 1 else suppose # prevRem / 2 
#                         rem = 0 if suppose<=1 else suppose-1
#                         dp[-1].append([curr, rem])
#                     else: 
#                         left = dp[-2][j-1][1]/2
#                         right = dp[-2][j][1]/2
#                         suppose = left + right
#                         curr = 1 if suppose >= 1 else suppose # prevRem / 2 
#                         rem = 0 if suppose<=1 else suppose-1
#                         dp[-1].append([curr, rem])
#             #print(dp)            
#             return dp[-1][query_glass][0]




# previous approach

# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         if poured ==0:
#             dp = [[[0,0]]] #[current, remaining]
#         else:
#             dp = [[[1, poured-1]]]
#         if query_row == 0:
#             return dp[0][0][0] # [row, element, curr]
#         else:
#             for i in range(1, query_row+1):
#                 dp.append([])
#                 for j in range(i+1): #add for each cup
#                     if j == 0: # rem = prevrem -1
#                         suppose = dp[-2][0][1]/2
#                         curr = 1 if suppose >= 1 else suppose # prevRem / 2 
#                         rem = 0 if suppose<=1 else suppose-1
#                         dp[-1].append([curr, rem])
#                     elif j == i:
#                         suppose = dp[-2][-1][1]/2
#                         curr = 1 if suppose >= 1 else suppose # prevRem / 2 
#                         rem = 0 if suppose<=1 else suppose-1
#                         dp[-1].append([curr, rem])
#                     else: 
#                         left = dp[-2][j-1][1]/2
#                         right = dp[-2][j][1]/2
#                         suppose = left + right
#                         curr = 1 if suppose >= 1 else suppose # prevRem / 2 
#                         rem = 0 if suppose<=1 else suppose-1
#                         dp[-1].append([curr, rem])
#             #print(dp)            
#             return dp[-1][query_glass][0]



