def findCircleNum(M: 'List[List[int]]'):
    def dfs(check_arr, M, curr_row, curr_col):
        if check_arr[curr_row][curr_col] == 1: #it has been visited from the parent, to avoid infinite loop
            return -1
        check_arr[curr_row][curr_col] = 1

        for c in range(curr_col):
            if M[curr_row][c] == 1:
                dfs(check_arr, M, c, curr_row) #transpose, starting from the friend cell

        for c in range(curr_col, len(M)):
            if M[curr_row][c] == 1:
                dfs(check_arr, M, c, curr_row) #transpose, starting from the friend cell

        return -1


    cnt = 0
    x = len(M)
    check_arr  = [[0 for _ in range(x)] for _ in range(x)] #0 means it has never been visited, 1 means visited
    for r in range(len(M)):
        for c in range(len(M)):
            if M[r][c] == 1 and check_arr[r][c] == 0:
                cnt += 1
                _ = dfs(check_arr, M, r , c)


    return cnt


print(findCircleNum([[1, 1, 0],
                     [1, 1, 0],
                     [0, 0, 1]]))
print(findCircleNum([[1,1,0],
 [1,1,1],
 [0,1,1]]))

print(findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))