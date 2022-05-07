class Solution:
    def find132pattern(self, nums: 'List[int]') -> bool: # O( N | N )
        mi = [nums[0]]  #accumulate minn
        for i in range(1, len(nums)):
            mi.append(min(mi[-1], nums[i]))
        
        stk = [nums[-1]] # mono stk
        for i in range(len(nums)-2, -1, -1):
            while stk and nums[i] > stk[-1]: # if curr is greater than mono stk top (smallest in the stk)
                if mi[i] < stk.pop(): # mi < curr, and stk top is > mi
                    return True 
            stk.append(nums[i]) # add curr to the stk
        
        return False



# previous solution

# class Solution:
#     def find132pattern(self, nums: 'List[int]') -> bool:
#         if len(nums) < 3:
#             return False
#         else:
#             minStk = [float('inf')]
#             for i in range(1, len(nums)):  # smallest on the left
#                 minStk.append(min(nums[i - 1], minStk[-1]))
#             stk = []
#             for i in range(len(nums) - 1, -1, -1):
#                 curr = -float('inf')
#                 while stk and stk[-1] < nums[
#                     i]:  # find the one smaller than the current one, but larger than the one in the minStk
#                     curr = stk.pop()
#                 if curr > minStk[i]:
#                     return True
#                 stk.append(nums[i])
#             return False


# previous approach
# class Solution:
#     def find132pattern(self, nums: 'List[int]') -> bool:
#         if len(nums) < 3:
#             return False
#         minStk = [float('inf')]  # first item does not have a number on the left
#         minn = float('inf')
#         for i in range(1, len(nums)):
#             minStk.append(min(minn, nums[i - 1]))
#
#         stk = []
#         t = -float('inf')
#         for i in range(len(nums) - 1, -1, -1):
#             while stk and stk[-1] < nums[i]:  # find second largest on the right
#                 t = stk.pop()
#
#             if t > minStk[i]:  # this is the last popped one
#                 return True
#             stk.append(nums[i])
#
#         return False
