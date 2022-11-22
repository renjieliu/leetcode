class Solution:
    def numSquares(self, n: int) -> int: # O( N**(3/2) | N )
        dp = [0] + [float('inf')] * n # initialize the dp and [0 squares to form 0], dp[0] = 0
        stk = [_**2 for _ in range(1, int(n**0.5)+1)] # N**(1/2) 
        for i in range(1, n+1): #for each number, find the minimum required, O( N )
            for s in stk: # O( N**(1/2) )  
                if i-s >= 0:
                    dp[i] = min(dp[i], dp[i-s] + 1)
                else: 
                    break
        return dp[-1]
    




# previous solution

# class Solution:
#     def numSquares(self, n: int) -> int: # O( N**(3/2) | N )
#         stk = [_**2 for _ in range(1, int(n**0.5)+1)] 
#         dp = [0, 1]  #[0 squares to form 0, 1 square to form 1]
#         for i in range(2, n+1): #for each number, find the minimum required
#             curr = float('inf')
#             for s in stk:
#                 if i-s >= 0:
#                     curr = min(curr, dp[i-s] + 1)
#             dp.append(curr)
#         return dp[-1]
    


# previous solution

# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [0] #initialize the dp, 0 as a dummy placeholder, to make the array lkp easier
#         lkp = []
#         for i in range(1, int(n**0.5) +1):
#             lkp.append(i**2)

#         for i in range(1, n+1): #to check the min to construct current number.
#             curr = float('inf')
#             for v in lkp: 
#                 if v <= i:
#                     if i % v == 0:
#                         curr = min(curr, i//v)
#                     else:
#                         curr = min(curr, i//v + dp[i%v]) #perfect square + remaining
#                 else:
#                     break
#             dp.append(curr)
#             # print(i, curr)
#         return dp[-1]
    


# previous approach
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [0] + [float('inf')]*n
#         for i in range(1, n+1):
#             dp[i] = 1+ min( dp[i-j**2] for j in range(1, int(i**0.5)+1) )
#         return dp[n]


# previous approach 
# def numSquares(n: int) -> int:
#     arr = [float('inf')] * (n + 1)
#     arr[0] = 0

#     for i in range(1, n+1):
#         arr[i] = min(arr[i-j*j] for j in range(1, int(i**0.5)+1)) + 1

#     return arr[n]


# print(numSquares(12))
# print(numSquares(4781))
# print(numSquares(47814))
# print(numSquares(7927))




