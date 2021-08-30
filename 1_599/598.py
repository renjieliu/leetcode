class Solution:
    def maxCount(self, m: int, n: int, ops: 'List[List[int]]') -> int:
        # greedy, to find the min(r) and min(c) in ops - these are the most changed elements
        return (min(a for a, b in ops) * min(b for a, b in ops)) if ops else m*n


# previous approach
# def maxCount(m, n, ops):
#     """
#     :type m: int
#     :type n: int
#     :type ops: List[List[int]]
#     :rtype: int
#     """
#     M = [[0]*m]*n
#
#     if len(ops) == 0:
#         return m*n
#     else:
#         min_1 = ops[0][0]
#         min_2 = ops[0][1]
#
#         for i in ops:
#             if i[0]< min_1:
#                 min_1 = i[0]
#             if i[1]< min_2:
#                 min_2 = i[1]
#
#         return min_1*min_2
#
# print(maxCount(5000,5012, [[2,2],[3,3], [1,4], [4,8], [16,16],[1121, 1213]]))
#
#
#
