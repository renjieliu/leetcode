def minFallingPathSum(A: 'List[List[int]]'):
    if len(A) ==1:
        return min(A[-1])

    B = A.copy()
    for r in range(1, len(A)):
        for c in range(len(A[0])):
            if c ==0:
                B[r][c] = min(A[r-1][c], A[r-1][c+1]) +A[r][c]
            elif c==len(A[0])-1:
                B[r][c] = min(A[r - 1][c], A[r - 1][c-1]) + A[r][c]
            else:
                B[r][c] = min(A[r - 1][c], A[r - 1][c - 1], A[r-1][c+1]) + A[r][c]

    return min(B[-1])

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))

