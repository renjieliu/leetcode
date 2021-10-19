def bin2dec(arr):
    output = 0

    for i in range(len(arr)-1, -1 , -1):
        power = (len(arr)-(i+1))
        output+=( arr[i]  * (2**power) )

    return output


def matrixScore(A: 'List[List[int]]'):
    B = A[:]
    #for rows, make the first digit to 1
    for r in range(len(A)):
        if A[r][0] == 0:
            for c in range(len(A[0])):
                B[r][c] = abs(A[r][c]-1)

    #for columns, make more 1s than 0s.
    for c in range(len(A[0])):
        sumCol = sum( [B[_][c] for _ in range(len(B))   ]       )
        if sumCol <= len(A)//2: # more 0 than 1. "<=" will also cover if the row%2!=0
            for r in range(len(A)):
                B[r][c] = abs(B[r][c]-1)

    output = 0
    for j in A:
        output += bin2dec(j)

    return output

print(matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
print(matrixScore([[1,1,1,1],[1,0,1,0],[1,1,0,0]]))




