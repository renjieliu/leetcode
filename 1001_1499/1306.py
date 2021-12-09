class Solution:
    def canReach(self, arr: 'List[int]', start: int) -> bool:
        def helper(dp, arr, loc):
            if loc in dp:
                return dp[loc] 
            else:
                dp[loc] = 0
                if loc >= len(arr) or loc < 0:
                    dp[loc] = 0
                else: 
                    if (loc+arr[loc] < len(arr) and arr[loc+arr[loc]] == 0) or (loc-arr[loc] > -1 and arr[loc-arr[loc]] == 0):
                        dp[loc] = 1
                    else: # if current cannot reach 0, then try both directions
                        dp[loc] += helper(dp, arr, loc+arr[loc])
                        if dp[loc] == 0 :
                            dp[loc] += helper(dp, arr, loc-arr[loc])
                    
                return dp[loc]
            
        dp = {}
        helper(dp, arr, start)
        # print(dp)
        return dp[start]

                

# previous approach
# class Solution:
#     def canReach(self, arr: 'List[int]', start: int) -> bool:
#         def dfs(check, curr_pos, dp, start):
#             # print(curr_pos)
#             if curr_pos == start:
#                 return 1
#             elif dp[curr_pos] == [] or check[curr_pos] == 1:
#                 return 0
#             else:
#                 check[curr_pos] = 1
#                 for i in dp[curr_pos]:  # in order to reach t,  find all the possible source for t
#                     if dfs(check, i, dp, start) == 1:
#                         return 1
#                 return 0

#         target = []
#         check = [0 for _ in range(len(arr))]  # to avoid [1,1,1,1], which could cause infinite loop
#         dp = [[] for _ in range(len(arr))]  # hold the possible source to reach current position
#         for i in range(len(arr)):
#             if arr[i] == 0:
#                 target.append(i)
#             else:
#                 if -1 < arr[i] + i < len(arr):
#                     dp[arr[i] + i].append(i)
#                 if -1 < i - arr[i] < len(arr):
#                     dp[i - arr[i]].append(i)
#         # print(target, '--- ' , dp)
#         if target == []:
#             return False
#         else:
#             for t in target:  # all the 0's in the arr
#                 if dfs(check, t, dp, start) == 1:
#                     return True
#             return False






































