class Solution:
    def minProductSum(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        nums1.sort()
        nums2.sort(reverse = True)
        output = 0
        while nums1:
            output += nums1.pop() * nums2.pop()
        return output
