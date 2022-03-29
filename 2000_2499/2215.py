class Solution:
    def findDifference(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[List[int]]':
        nums1 = set(nums1) # make it a set to speed up the look up
        nums2 = set(nums2) # make it a set to speed up the look up
        return [[i for i in nums1 if i not in nums2], [i for i in nums2 if i not in nums1]]
    
    
