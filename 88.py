class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def insert(arr, index, num):
            for i in range(len(arr)-1, index, -1):
                arr[i] = arr[i-1]
            arr[index] = num
        i = j = 0
        while j < n:
            curr = nums2[j]
            while nums1[i] < curr and i < m+j: # m+j is current length of the total items in nums1
                i+=1
            insert(nums1, i, curr)
            j+=1



# previous approach
# def merge(nums1: 'List[int]', m: int, nums2: 'List[int]', n: int):
#     p1 = 0
#     p2 = 0
#     cnt = 0
#     if m==0:
#         nums1[:] = nums2[:n]
#     else:
#         while p2 < len(nums2):
#             while p1 < len(nums1):
#                 if nums1[p1] < nums2[p2]:
#                     p1 += 1
#                     if p1 > m - 1 + cnt:  # all the rest elements are greater than the largest element in nums1
#                         while nums2:
#                             nums1.pop()
#                             nums1.insert(p1, nums2.pop(0))
#                             p1 += 1
#                         p1 = len(nums1)
#                         p2 = len(nums2)
#                         break
#                 else:
#                     nums1.pop()
#                     nums1.insert(p1, nums2.pop(0))
#                     p1 += 1
#                     cnt += 1
#                     break
#
#
#
#
# nums1 = [0,0,0,0,0]
# m=0
# nums2 = [1,2,3,4,5]
# n=5
# merge(nums1, m, nums2, n)
# print(nums1)
#
# nums1 = [1,2,3,0,0,0]
# m=3
# nums2 = [2,5,6]
# n=3
# merge(nums1, m, nums2, n)
#
#
# print(nums1)


