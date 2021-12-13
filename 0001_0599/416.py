class Solution:
    def canPartition(self, nums: 'List[int]') -> bool:
        if sum(nums)%2 == 1 or len(nums) == 1:
            return False
        else:
            val = sum(nums) // 2
            # cnt = [0]
            def helper(dp, val, arr, curr): # dp to check if current total was seen before
                if curr in dp:
                    return dp[curr]
                else:
                    dp[curr] = 0
                    if curr == val:
                        dp[curr] = 1
                    elif curr < val:
                        for i in range(len(arr)):
                            if helper(dp, val, arr[i+1:], curr+arr[i]) == 1 or helper(dp,val, arr[i+1:], curr) == 1:
                                dp[curr] = 1
                                break
                    return dp[curr]
                
            return helper({}, val, nums, 0) 


# previous approach
# class Solution:
#     def canPartition(self, nums: 'List[int]') -> bool:
#         if len(nums) == 1 or sum(nums) %2 == 1 or max(nums) > sum(nums) // 2:
#             return False
#         else:
#             target = sum(nums) // 2
#             def dfs(curr, target, rem, arr, dp):
#                 if curr == target: # found
#                     dp[curr] = True
#                     return True
#                 elif curr in dp:
#                     return dp[curr]

#                 else:
#                     for i, a in enumerate(arr):
#                         if a <= rem:
#                             if dfs(curr+a, target, rem - a, arr[i+1:], dp ) == True:
#                                 dp[curr] = True
#                                 return dp[curr]
#                             else:
#                                 dp[curr] = False
#                     return False

#         nums.sort()
#         dp = {}
#         return dfs(nums[0], target, target - nums[0], nums[1:], dp)
