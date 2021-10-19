class Solution:
    def maximumUniqueSubarray(self, nums: 'List[int]') -> int:
        output = 0
        curr = 0
        lkp= set()
        l = r = 0
        while r < len(nums):
            while nums[r] in lkp and l <= r:
                curr -= nums[l]
                lkp.remove(nums[l])
                l+=1
            lkp.add(nums[r])
            curr+=nums[r]
            output = max(output, curr)
            r+=1
        return output

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

