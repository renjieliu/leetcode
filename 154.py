class Solution:
    def findMin(self, nums: 'List[int]') -> int:
        if len(nums)<=2: return nums[0] if nums[0] <=nums[-1] else nums[-1]
        s = 0
        e = len(nums)-1
        while s<=e:
            mid = (s+e)//2
            if mid+1 <= len(nums)-1:
                if nums[mid] <= nums[mid+1]: #pivot either on the left or right
                    return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))
                elif nums[mid] > nums[mid+1]: #current is the pivot
                    return nums[mid+1]
            else:
                break




# previous approach
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         def find(arr, ref):  # in the arr, to find a number smaller than the ref
#             if len(arr) == 0:
#                 return float('inf')
#             s = 0
#             e = len(arr) - 1
#             t = float('inf')
#             while s <= e:
#                 mid = (s + e) // 2
#                 if arr[mid] < ref:
#                     t = arr[mid]
#                     e = mid - 1
#                 elif arr[mid] > ref:
#                     s = mid + 1
#                 elif arr[mid] == ref:
#                     l = find(arr[:mid], ref)  # to find in left, if not found, it becomes float('inf')
#                     r = find(arr[mid + 1:], ref)  # to find in the right part, if not found it becomes float('inf')
#                     return min(l, r)
#             return t  # if not found it becomes float('inf')
#
#         return min(find(nums, nums[0]), nums[0])