class Solution:
    def searchInsert(self, nums: 'List[int]', target: int) -> int: 
        s = 0
        e = len(nums)-1 
        while s <= e: #binary search to find the first place >= than the target
            mid = s - (s-e)//2
            if nums[mid] >= target:
                e = mid - 1 
            else:
                s = mid +1
        return s 
    


# previous approach
# class Solution:
#     def searchInsert(self, nums: 'List[int]', target: int) -> int:
#         s = 0
#         e = len(nums) - 1
#         while s <= e: #bin_search
#             mid = (s + e) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 e = mid - 1
#             else:
#                 s = mid + 1
#         return s



    # old approach, O(n)
# def searchInsert(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     for i in range(0, len(nums)):
#         if nums[i] >= target :
#             return i
#
#     return len(nums)
#
#
# print(searchInsert( [1], 0) )
#
#
#
