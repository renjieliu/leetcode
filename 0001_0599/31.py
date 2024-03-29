class Solution:
    def nextPermutation(self, nums: 'List[int]') -> None: # O(N | 1)
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, s, e):
            total = e-s+1 
            for i in range(total//2):
                arr[s+i], arr[s+total-1-i] = arr[s+total-1-i], arr[s+i]
        
        if len(nums) > 1 :
            find = 0 
            for i in range(len(nums)-2, -1, -1): # to find the decrease
                if nums[i] < nums[i+1]:
                    find = 1 
                    pivot = nums[i]
                    loc = i
                    break 
            if find == 0: #no decrease find
                reverse(nums, 0, len(nums)-1)
            else:
                # print(pivot, loc)
                for p in range(len(nums)-1, -1, -1): #find the first number on the right side, smaller than nums[i]
                    if nums[p] > pivot:
                        nums[p], nums[loc] = nums[loc], nums[p]
                        reverse(nums, loc+1, len(nums)-1) #reverse the loc+1 to end, is like sort, as it's monotone
                        break
                    


# previous solution

# class Solution:
#     def nextPermutation(self, nums: 'List[int]') -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         def swap(arr, A, B):
#             t = arr[A]
#             arr[A] = arr[B]
#             arr[B] = t

#         def bubble_sort(arr, s, e):
#             for i in range(e, s - 1, -1):
#                 for j in range(i - 1, s - 1, -1):
#                     if arr[j] > arr[i]:
#                         swap(arr, j, i)

#         i = 1
#         pos1, pos2 = None, None  # pos2 > pos1
#         while i < len(nums):  # to swap the last increase digits. If not find any, reverse the whole thing.
#             if nums[i] > nums[i - 1]:
#                 pos1 = i - 1
#                 pos2 = i
#             i += 1
#         if pos1 != None:
#             i = pos2
#             m = float('inf')
#             while i < len(
#                     nums):  # find the least number > than nums[pos1], on the right side of, and pump that one to the first.
#                 if nums[i] > nums[pos1] and nums[i] < m:
#                     pos2 = i
#                     m = nums[i]
#                 i += 1
#             swap(nums, pos1, pos2)
#             # need to sort the nums[pos1+1:]
#             bubble_sort(nums, pos1 + 1, len(nums) - 1)


#         else:  # reverse the nums
#             i = 0
#             while i < len(nums) // 2:
#                 swap(nums, i, len(nums) - 1 - i)
#                 i += 1






