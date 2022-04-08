class Solution:
    def minProductSum(self, nums1: 'List[int]', nums2: 'List[int]') -> int: #O(nlogn)
        nums1.sort() #greedy, smallest * largest 
        nums2.sort(reverse = True)
        output = 0
        for i in range(len(nums1)):
            output += (nums1[i] * nums2[i])
        return output

    

# previous solution

# class Solution:
#     def minProductSum(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
#         nums1.sort()
#         nums2.sort(reverse = True)
#         output = 0
#         while nums1:
#             output += nums1.pop() * nums2.pop()
#         return output
