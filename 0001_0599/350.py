class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        hmp_a = {}
        hmp_b = {}
        for n in nums1:
            if n not in hmp_a:
                hmp_a[n] = 0
            hmp_a[n] += 1
        for n in nums2:
            if n not in hmp_b:
                hmp_b[n] = 0
            hmp_b[n] += 1
        output = []
        for k, v in hmp_a.items():
            if k in hmp_b:
                output += [k] * min(v, hmp_b[k])
        return output





# previous approach
# def intersect(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: List[int]
#     """
#     output = list()
#     x1 = list(nums1)
#     x2 = list(nums2)
#
#     if len(x1) > len(x2):
#         for i in range(0, len(x1) - len(x2)):
#             x2.append("`")
#     elif len(x2) > len(x1):
#         for i in range(0, len(x2) - len(x1)):
#             x1.append("`")
#
#     for i in x1:
#         if i in x2:
#             x2[x2.index(i)] = '!'
#             output.append(i)
#         if i =="`":
#             break
#
#     return output
#
# print(intersect([2,2], [1,2,3, 2, 2, 1]))
#
#
#
