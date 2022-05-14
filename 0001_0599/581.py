class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> int: #O(N | N)
        stk = [] # to record the smallest location 
        left = float('inf')
        for i in range(len(nums)):
            while stk and nums[stk[-1]] > nums[i]:
                left = min(left, stk.pop())
            stk.append(i)
        stk = [] # to recrord the largest location
        right = -float('inf')
        for i in range(len(nums)-1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                right = max(right, stk.pop())
            stk.append(i)
        
        return 0 if left == float('inf') else right - left + 1 
    


# previous solution

# class Solution:
#     def findUnsortedSubarray(self, nums: 'List[int]') -> int:  #O(N | N)
#         stk = [] #record the current smallest location
#         left = float('inf')
#         for i in range(len(nums)):
#             while stk and nums[stk[-1]] > nums[i]:
#                  left = min(left, stk.pop())
#             stk.append(i)        
        
#         stk = [] # record the current  largest location
#         right = -float('inf')
#         for i in range(len(nums)-1, -1, -1):
#             while stk and nums[stk[-1]] < nums[i]:
#                 right = max(right, stk.pop())
#             stk.append(i)
        
#         return right - left + 1 if left != float('inf') else 0
    
    
    
# previous solution

# class Solution:
#     def findUnsortedSubarray(self, nums: 'List[int]') -> int:
#         if len(nums) == 1: return 0
#         stk = []
#         left = float('inf')
#         right = -float('inf')
#         i = 0
#         while i < len(nums):
#             while stk and nums[i] < nums[stk[-1]]: #keep popping the stack, until meeting a smaller
#                 left = min(left, stk.pop())
#             stk.append(i)
#             i+=1

#         j = len(nums)-1
#         stk = []
#         while j > -1:
#             while stk and nums[j] > nums[stk[-1]] : #keep popping the stack until meeting a larger..
#                 right = max(right, stk.pop() )
#             stk.append(j)
#             j-=1

#         # print(left, right)
#         output = abs(right - left) + 1
#         return 0 if output == float('inf') else output




# previous approach
# class Solution:
#     def findUnsortedSubarray(self, nums: 'List[int]') -> int:
#         arr = []
#         for n in nums:
#             arr.append(n)
#         arr.sort() #the reference array
#         right = 0
#         left = len(nums)-1
#         while right < len(arr): #find the first mismatch from right side
#             if arr[right] != nums[right]:
#                 break
#             right+=1
#         right = len(nums) - 1 if right == len(nums) else right
#
#         while left > -1: #find the first mismatch from left side
#             if arr[left] != nums[left]:
#                 break
#             left -= 1
#         left = 0 if left == -1 else left
#
#         #print(left, right)
#         return 0 if right == len(nums)-1 and left == 0 else abs(left - right) + 1
#
