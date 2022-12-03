class Solution:
    def sumSubarrayMins(self, arr: 'List[int]') -> int: # O( N | N )
        dp = [0] * len(arr)
        stk = [] # [val, loc]
        for i in range(len(arr)):
            curr = arr[i]
            while stk and stk[-1][0] >= curr:
                stk.pop()
            if stk: #there's a smaller number in the front
                prevSmallLoc = stk[-1][1] 
                total = (i - prevSmallLoc) * curr + dp[prevSmallLoc]
                dp[i] = total
            else: # current number is the smallest
                dp[i] = (i+1) * curr
            
            stk.append([curr, i])
            
        return sum(dp) % (10**9+7)


# previous solution

# class Solution:
#     def sumSubarrayMins(self, arr: 'List[int]') -> int: # O( N | N )
#         stk = [] # [n, loc]
#         dp = [0] * len(arr)
#         for i in range(len(arr)):
#             curr = arr[i]
#             while stk and stk[-1][0] >= curr: #keep popping the stk, until meeting the first one smaller than curr
#                 stk.pop()
#             if stk:
#                 dist = i - stk[-1][1] # to count how many element b/w current and the previous smaller
#                 currTotal = dist*curr # total sum of curr and the previous larger element
                
#                 dp[i] = dp[stk[-1][1]] + currTotal # curr is smaller than previous larger, so need to add the previous larger total

#             else: # this is the smallest number so far
#                 dp[i] = (i+1)*curr

#             stk.append([curr, i]) # add curr to the stack
            
#         return sum(dp) % (10**9+7) 


