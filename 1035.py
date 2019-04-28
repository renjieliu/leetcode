def maxUncrossedLines( A: 'List[int]', B: 'List[int]'):
    dp = [[0 for _ in range(len(A)+1)] for  _ in range(len(B)+1)]

    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if A[j-1] ==B[i-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]



print(maxUncrossedLines(A = [1,4,2], B = [1,2,4]))
print(maxUncrossedLines(A = [2,5,1,2,5], B = [10,5,2,1,5,2]))
print(maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]))