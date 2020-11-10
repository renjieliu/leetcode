class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        return [[_^1 for _ in r[::-1]] for r in A]


# previous approach
# def flipAndInvertImage(A):
#     """
#     :type A: List[List[int]]
#     :rtype: List[List[int]]
#     """
#     output = []
#     temp= []
#     for i in A :
#         for j in i[::-1]:
#             temp.append(abs(j-1))
#         output.append(temp)
#         temp = []
#     return output
#
# print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
# print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
