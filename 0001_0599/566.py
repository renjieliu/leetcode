class Solution:
    def matrixReshape(self, mat: 'List[List[int]]', r: int, c: int) -> 'List[List[int]]':
        if r*c != len(mat) * len(mat[0]):
            return mat
        else:
            arr = []
            for sr in range(len(mat)):
                for sc in range(len(mat[0])):
                    arr.append(mat[sr][sc])
            output = []
            for a in range(r):
                output.append([])
                for b in range(c):
                    output[-1].append(arr.pop(0))
            return output



# previous approach
# def matrixReshape(nums, r, c):
#     """
#     :type nums: List[List[int]]
#     :type r: int
#     :type c: int
#     :rtype: List[List[int]]
#     """
#     temp = []
#     output = [[]]
#     for i in nums:
#         for j in i:
#             temp.append(j)
#
#     if r*c != len(temp):
#         return nums
#
#     else:
#         e = 0
#         cnt = 0
#         now = 0
#         for i in temp:
#             cnt += 1
#             now += 1
#             if now > len(temp):
#                 return output
#             elif cnt <= c:
#                 output[e].append(i)
#             elif cnt > c :
#                 output.append([])
#                 e+=1
#                 output[e].append(i)
#                 cnt = 1
#
#
#     return output
#
# print( matrixReshape([[1,2,3,4,5,6,7,8,9,10], [11,2]],4,3))
#
