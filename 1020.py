def numEnclaves_dfs(done, A, sr, sc, output):
    if output[sr][sc] == 1 and done[sr][sc] == None:
        output[sr][sc] = 0
        done[sr][sc] = -1

        for r in range(sr + 1, len(A)):
            if numEnclaves_dfs(done, A, r, sc, output) == -1:
                break

        for r in range(sr - 1, -1, -1):
            if numEnclaves_dfs(done, A, r, sc, output) == -1:
                break

        for c in range(sc + 1, len(A[0])):
            if numEnclaves_dfs(done, A, sr, c, output) == -1:
                break

        for c in range(sc - 1, -1, -1):
            if numEnclaves_dfs(done, A, sr, c, output) == -1:
                break

    else:
        return -1


def numEnclaves(A: 'List[List[int]]'):
    done = [[None for _ in range(len(A[0]))] for _ in range(len(A))]
    output = A.copy()
    r = 0
    for c in range(len(A[0])):
        if done[r][c] == None and A[r][c] == 1:
            numEnclaves_dfs(done, A, r, c, output)

    r = len(A) - 1
    for c in range(len(A[0])):
        if done[r][c] == None and A[r][c] == 1:
            numEnclaves_dfs(done, A, r, c, output)

    c = 0
    for r in range(len(A)):
        if done[r][c] == None and A[r][c] == 1:
            numEnclaves_dfs(done, A, r, c, output)

    c = len(A[0]) - 1
    for r in range(len(A)):
        if done[r][c] == None and A[r][c] == 1:
            numEnclaves_dfs(done, A, r, c, output)

    res = 0
    for i in range(len(output)):
        res += sum(output[i])

    return res


print(numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
print(numEnclaves([[0,0,1,1,1,0,1,1,1,0,1],[1,1,1,1,0,1,0,1,1,0,0],[0,1,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,1,1,0,0,0,1],[0,0,1,0,1,1,0,0,1,0,0],[1,0,0,1,1,1,0,0,0,1,1],[0,1,0,1,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,1,0,0],[1,1,0,1,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,1,0,0,1]]))
