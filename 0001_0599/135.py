class Solution:
    def candy(self, ratings: 'List[int]') -> int: #O( N | 1 )
        if len(ratings) == 1:
            return 1
        else:
            gauss = lambda x: (x+1)*x//2 # sum from 1 to x
            output = 0 
            up = down = 0 #uphill or downhill
            prev = 0 
            for i in range(1, len(ratings)): # 1 up, -1 down, 0 flat
                curr = 1 if ratings[i] > ratings[i-1] else (-1 if ratings[i] < ratings[i-1] else 0) #check current is downhill or uphill
                if (prev > 0 and curr == 0) or (prev < 0 and curr >= 0): #update if it meets flat, or the downhill meets the uphill
                    output += gauss(down) + gauss(up) + max(down, up) #add the slope length and pick one for the peak / valley
                    up = 0 
                    down = 0
                
                if curr > 0:
                    up += 1 
                elif curr < 0:
                    down += 1
                elif curr == 0:
                    output += 1
                
                prev = curr

            output += gauss(up) + gauss(down) + max(up, down) + 1 #add the slope length and add the peak or valley, the +1 is the peak or valley
            return output
        
    
                    
                    
                
            


# previous solution

# class Solution:
#     def candy(self, ratings: 'List[int]') -> int:
#         if len(ratings) == 1:
#             return 1
#         dp = [None] * len(ratings)

#         def helper(dp, ratings, pos):  # this is to find the end of the decreasing slope
#             # print(dp)
#             if dp[pos] != None:
#                 return dp[pos]
#             else:
#                 if pos == len(dp) - 1:
#                     dp[pos] = 1 if ratings[-1] <= ratings[-2] else (dp[pos - 1] + 1)
#                 elif pos == 0:
#                     if ratings[pos] <= ratings[pos + 1]:
#                         dp[pos] = 1
#                     else:
#                         dp[pos] = 1 + helper(dp, ratings, pos + 1)
#                 else:  # compare with the neighbours, and get the result.
#                     if ratings[pos - 1] < ratings[pos] <= ratings[pos + 1]:
#                         dp[pos] = 1 + dp[pos - 1]
#                     elif ratings[pos + 1] < ratings[pos] <= ratings[pos - 1]:
#                         dp[pos] = 1 + helper(dp, ratings, pos + 1)
#                     elif ratings[pos] > ratings[pos + 1] and ratings[pos] > ratings[pos - 1]:
#                         dp[pos] = 1 + max(dp[pos - 1], helper(dp, ratings, pos + 1))
#                     elif ratings[pos] <= ratings[pos + 1] and ratings[pos] <= ratings[pos - 1]:
#                         dp[pos] = 1
#                 return dp[pos]

#         for i in range(len(ratings)):  # find candies for each one.
#             helper(dp, ratings, i)
#         # print(dp)
#         return sum(dp)






