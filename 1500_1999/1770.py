class Solution:
    def maximumScore(self, nums: 'List[int]', multipliers: 'List[int]') -> int: # O( M**2 | M**2 )
        arr = multipliers
        m = len(arr)
        n = len(nums)
        dp = [[0] * (m+1) for _ in range(m+1)] # intialize as m+1 to make dp[op + 1][left + 1] as 0, for the initial cases, where starting from take everything from the left 
        
        for op in range(m-1, -1, -1): #number of operations
            for left in range(op, -1, -1): #the location of left pointer
                right = n - 1 - (op - left) #the pointer on the right side of nums
                A = arr[op] * nums[left] + dp[op + 1][left + 1] #perform on the left, next move is left +1 and op+1
                B = arr[op] * nums[right] + dp[op + 1][left] # perform on the right, the left pointer stays the same
                dp[op][left] = max(A, B)
        return dp[0][0]


        

        
        
# class Solution: # TLE, with top down approach
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int: # O( M**2 | M**2 )
#         def helper(hmp, nums, s, arr):
#             n = len(arr)
#             if n == 0 :
#                 return 0 
#             elif (n, s) in hmp: 
#                 return hmp[(n, s)] #len(arr), start in nums
#             else:
#                 A = arr[0] * nums[0] + helper(hmp, nums[1:], s+1, arr[1:])
#                 B = arr[0] * nums[-1] + helper(hmp, nums[:-1], s, arr[1:])
#                 hmp[(n,s)] = max(A, B)
#                 return hmp[(n, s)]
#         return helper({},  nums, 0,  multipliers)

