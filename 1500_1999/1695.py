class Solution:
    def maximumUniqueSubarray(self, nums: 'List[int]') -> int: # O(N | N)
        pre = [0]
        for n in nums: # prefix sum
            pre.append(pre[-1] + n)
        output = 0 
        l = 0 
        seen = set()
        for r in range(len(nums)): #check if curr is seen. Keep taking out the left, and check the range sum
            while l < r and nums[r] in seen:
                seen.remove(nums[l])
                l += 1 
            seen.add(nums[r]) 
            output = max(output, pre[r+1] - pre[l])
        return output 
    

# previous solution

# class Solution:
#     def maximumUniqueSubarray(self, nums: 'List[int]') -> int:
#         output = 0
#         curr = 0
#         lkp= set()
#         l = r = 0
#         while r < len(nums):
#             while nums[r] in lkp and l <= r:
#                 curr -= nums[l]
#                 lkp.remove(nums[l])
#                 l+=1
#             lkp.add(nums[r])
#             curr+=nums[r]
#             output = max(output, curr)
#             r+=1
#         return output

# previous approach
# class Solution:
#     def maximumUniqueSubarray(self, nums: 'List[int]') -> int:
#         l = r = 0
#         output = -float('inf')
#         lkp = set()
#         window = 0
#         while r < len(nums) :
#             curr = nums[r]
#             if curr not in lkp:
#                 lkp.add(curr)
#                 window+=curr
#                 output = max(output, window)
#             else:
#                 while nums[l] != curr:
#                     lkp.remove(nums[l])
#                     window -= nums[l]
#                     l+=1
#                 l+=1 #move it one more time to the start of curr window
#                 lkp.add(curr)
#                 output=max(output, window)
#             r+=1
#         return output

