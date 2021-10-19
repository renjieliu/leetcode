def maxDistance(grid: 'List[List[int]]'):
    w = len(grid)
    if w == 1:
         return -1
    dp =[[300 for _ in range(w)] for _ in range(w) ]
    for r in range(w):
        for c in range(w):
            if grid[r][c] ==1:
                dp[r][c] =0
            else: #if current grid is water
                if r==0:
                    if c==0 :
                        dp[r][c] = min(dp[r][c],  300)
                    else:
                        dp[r][c] = min(dp[r][c-1]+1, 300)
                else:
                    if c ==0:
                        dp[r][c] = min(dp[r-1][c] + 1, 300)
                    else:
                        dp[r][c] = min(dp[r][c-1]+1, dp[r-1][c]+1,300)
    #print(dp)
    for r in range(w-1, -1,-1):
        for c in range(w-1, -1,-1):
            if r == w-1:
                if c == w-1 :
                    dp[r][c] = min(dp[r][c], 300)
                else:
                    dp[r][c] = min(dp[r][c], dp[r][c + 1] + 1, 300)

            else:
                if c ==w-1 :
                    dp[r][c] = min(dp[r][c], dp[r+1][c]+1, 300)
                else:
                    dp[r][c] = min(dp[r][c], dp[r][c+1] + 1, dp[r + 1][c] + 1, 300)
    #print(dp)
    output = 0

    for r in range(w):
        for c in range(w):
            output = max(dp[r][c], output)

    return output if output not in [0,300] else -1


print(maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
print(maxDistance([[1,0,0],[0,0,0],[0,0,0]]))
print(maxDistance([[0,0,0],[0,0,0],[0,0,0]]))
print(maxDistance([[1,1,1],[1,1,1],[1,1,1]]))
print(maxDistance([[1,0,0,0,0,1,0,0,0,1],[1,1,0,1,1,1,0,1,1,0],[0,1,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1],[0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,1,1,0,0],[1,1,0,1,1,1,1,1,0,0]]))



