class Solution:
    def findPeakElement(self, nums: 'List[int]') -> int:
        s = 0
        e = len(nums)-1
        while s <= e: # binary search, use the larger number as the limit each time, until find the peak number
            mid = (s+e)//2
            left = nums[mid-1] if mid > 0 else -float('inf')
            right = nums[mid+1] if mid < len(nums)-1 else -float('inf')
            if nums[mid] > left and nums[mid] > right:
                return mid
            else:
                if left >= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
        return s


#the O(N) approach
#         if len(nums) == 1:
#             return 0
#         for i in range (len(nums)):
#             if i ==0 and nums[i] > nums[i+1]:
#                 return i
#             elif i == len(nums)-1 and nums[i] > nums[i-1]:
#                 return i
#             elif nums[i]> nums[i-1] and nums[i] > nums[i+1]:
#                 return i

