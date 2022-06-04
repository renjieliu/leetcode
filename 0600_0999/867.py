class Solution:
    def transpose(self, matrix: 'List[List[int]]') -> 'List[List[int]]': #O(MN | MN)
        dp = [[_ for _ in matrix] for _ in matrix[0]] # form the new matrix. Original r is new c, and original c is the new r
        for r in range(len(dp)):
            for c in range(len(dp[0])): #put the transposed element to the new matrix
                dp[r][c] = matrix[c][r]
        return dp



# previous solution

# def transpose(A: 'List[List[int]]'):
#     c_cnt = len(A[0])
#     r_cnt = len(A)
#     output = []

#     for i in range(0, c_cnt):
#         output.append([])
#         for j in range(0, r_cnt):
#             output[i].append(A[j][i])

#     return output

# print(transpose([[1,2,3],[4,5,6]]))



