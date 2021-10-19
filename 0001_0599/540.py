class Solution:
    def singleNonDuplicate(self, nums: 'List[int]') -> int:
        s = 0
        e = len(nums)-1
        while s<=e :
            mid = (s+e)//2
            if (mid < len(nums)-1 and mid%2 == 0 and nums[mid+1] == nums[mid]) or ( mid > 0 and mid%2 == 1 and nums[mid] == nums[mid-1]): # this is the good part, the problem is on the right
                s = mid+1
            else:
                e = mid-1 # omit the possible candidate, if nothing on the left works,then final s or e+1 is the possible candidate.
        return nums[s] # same as return num[e+1]





# OLD Solution with O(n)
# class Solution:
#     def singleNonDuplicate(self, nums: 'List[int]') -> int:
#         curr = nums[0]
#         for i in range(1, len(nums)):
#             curr ^= nums[i]
#         return curr
#


#OLD Solution - O(n), T(n)
# def singleNonDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     cnt = 0
#     for i in range(len(nums) - 1):
#         cnt += 1
#         if cnt == 2:
#             if nums[i] != nums[i - 1]:
#                 return nums[i - 1]
#             else:
#                 cnt = 0
#     return nums[-1]
#
#
# print(singleNonDuplicate([1,1,2]))
# print(singleNonDuplicate([1,2,2]))
# print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
# print(singleNonDuplicate([3,3,7,7,10,11,11]))


