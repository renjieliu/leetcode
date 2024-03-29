class Solution:
    def minFallingPathSum(self, matrix: 'List[List[int]]') -> int: # O( MN | N ) 
        dp = matrix[-1]  # only using 1 row to store the min up to current row
        for r in range(len(matrix)-2, -1, -1): # work backwards from the last row
            curr = []
            for c in range(len(matrix[0])):
                A = max(0, c-1) #down left
                B = min(len(matrix[0])-1, c+1) # right right
                curr.append(min( matrix[r][c] + dp[c], matrix[r][c]+dp[A], matrix[r][c] +dp[B]))
            dp = curr 
        
        return min(dp)
                    




# previous solution


# def minFallingPathSum(A: 'List[List[int]]'):
#     if len(A) ==1:
#         return min(A[-1])

#     B = A.copy()
#     for r in range(1, len(A)):
#         for c in range(len(A[0])):
#             if c ==0:
#                 B[r][c] = min(A[r-1][c], A[r-1][c+1]) +A[r][c]
#             elif c==len(A[0])-1:
#                 B[r][c] = min(A[r - 1][c], A[r - 1][c-1]) + A[r][c]
#             else:
#                 B[r][c] = min(A[r - 1][c], A[r - 1][c - 1], A[r-1][c+1]) + A[r][c]

#     return min(B[-1])

# print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))




