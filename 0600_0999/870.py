class Solution:
    def advantageCount(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        arr_a = []
        for a in A:
            arr_a.append(['a', a])
        arr_b = []
        for i, b in enumerate(B):
            arr_b.append(['b', b, i])
        A.sort()
        arr = sorted(arr_a + arr_b, key = lambda x: x[1])
        prev = []
        hmp_b = {} #for the loc i, the value from a to pick
        for a in arr[::-1]:
            if a[0]=='a':
                prev.append(a[1])
            else:
                if prev:
                    hmp_b[a[2]] = prev.pop(0)
                else: #there's no number larger than curr b, then just use the smallest number from A
                    hmp_b[a[2]] = A.pop(0)
        output = []
        for i, c in enumerate(B):
            output.append(hmp_b[i])
        return output




# previous approach
# class Solution:
#     def advantageCount(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
#         ref_A = []
#         for a in A:
#             ref_A.append(['a', a])  # [a, a_value]
#         ref_A.sort(key=lambda x: x[1])
#         ref_B = []
#         i = 0
#         while i < len(B):
#             b = B[i]
#             ref_B.append(['b', b, i])  # [b, value, pos]
#             i += 1
#         ref = sorted(ref_A + ref_B, key=lambda x: x[1])  # this will hold the position and for each a and b
#         prev = []  # to save all the a > b
#         hmp_b = {}
#         for i in range(len(ref) - 1, -1, -1):
#             if ref[i][0] == 'a':
#                 prev.append(ref[i][1])
#             elif ref[i][0] == 'b':
#                 if prev == []:  # current b is > than any a, we just need to put the smallest available a
#                     hmp_b[ref[i][2]] = ref_A[0][1]
#                     ref_A.pop(0)
#                 else:
#                     if prev[-1] > ref[i][1]:  # only when the found a > the current b
#                         hmp_b[ref[i][2]] = prev.pop(0)
#                     else:
#                         hmp_b[ref[i][2]] = ref_A[0][1]
#                         ref_A.pop(0)
#         # print(ref)
#         output = []
#         i = 0
#         while i < len(B):
#             output.append(hmp_b[i])
#             i += 1
#         return output
#
#
#
#
#
#
#
