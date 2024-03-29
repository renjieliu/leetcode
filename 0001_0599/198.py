class Solution:
    def rob(self, nums: 'List[int]') -> int: # O( N | N )
        def helper(dp, idx, arr):
            if idx in dp:
                return dp[idx]
            dp[idx] = 0 
            if idx >= len(arr):
                return dp[idx]
            else: # take current, go to idx+2, or ignore current, go to idx+1
                A = arr[idx] + helper(dp, idx+2, arr)
                B = helper(dp, idx+1, arr)
                dp[idx] = max(A, B)
                return dp[idx]
        
        return helper({}, 0, nums)




# previous solution

# class Solution:
#     def rob(self, nums: 'List[int]') -> int: #dp approach
#         if len(nums) <= 2:
#             return max(nums)
#         a = nums[0] 
#         b = nums[1]
#         output = max(a, b)
#         for n in nums[2:]:
#             c = max(n+a, b) #max at current, either take a or use b as is
#             output = max(output, c)
#             a = max(a, b) 
#             b = max(b, c)
#         return output



# previous approach
# class Solution:
#     def rob(self, nums: 'List[int]') -> int:
#         def helper(hmp, loc, arr):
#             if loc in hmp:
#                 return hmp[loc]
#             elif loc >= len(arr):
#                 hmp[loc] = 0 
#                 return hmp[loc]
#             else:
#                 hmp[loc] = 0 
#                 for i in range(loc, len(arr)):
#                     A = arr[loc] + helper(hmp, i+2, arr) # take current and move on
#                     B = helper(hmp, i+1, arr) # just move on to the next one
#                     hmp[loc] = max(hmp[loc], A, B)
#                 return hmp[loc]
        
#         hmp = {}
#         helper(hmp, 0, nums)
#         # print(hmp)
#         return hmp[0]


# previous approach

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if nums == [] :return 0
#         elif len(nums) <=2: return max(nums)
        
#         def dp(arr, i, mem):
#             if i >=len(mem):
#                 return 0
#             elif mem[i] != -float('inf'): 
#                 return mem[i]
#             elif len(arr[i:]) ==0 :
#                 return 0           
#             elif len(arr[i:]) == 1 :
#                 return arr[i]
#             else:
#                 A = arr[i] + dp(arr, i+2, mem)
#                 B = arr[i+1] + dp(arr, i+3, mem)
#             # print(i, A, B)
#             mem[i] = max(A, B)
#             return mem[i]
        
#         mem = [-float('inf')] * len(nums)
#         dp(nums, 0, mem)
#         return mem[0]



# previous approach
# def rob(nums: 'List[int]'):
#     if len(nums)==0:
#         return 0
#     elif len(nums)==1:
#         return nums[0]
#     elif len(nums)==2:
#         return max(nums[0], nums[1])
#     opt = [0]*3

#     opt[0] = nums[0]
#     opt[1] += max(opt[0], nums[1])

#     for i in range(2, len(nums)):
#         opt[2] = max(nums[i] + opt[0], opt[1])
#         opt[0] = opt[1]  #shift the position after calculation
#         opt[1] = opt[2]

#     return opt[2]


# print(rob([1,2,3,1]))
# print(rob([1,1]))
# print(rob([0]))
# print(rob([]))
# print(rob([2,7,9,3,1]))