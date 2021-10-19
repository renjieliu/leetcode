def maxIncreaseKeepingSkyline(grid: 'List[List[int]]'):
    #angle 1, look from left:
    max_1 = []
    for i in range(0, len(grid)):
        max = 0
        for j in range(0, len(grid)):
            if grid[i][j]>max:
                max = grid[i][j]
        max_1.append(max)

    #angle 2, look from top:
    max_2 = []
    for i in range(0,len(grid)):
        max = 0
        for j in range(0,len(grid)):
            if grid[j][i] > max:
                max = grid[j][i]

        max_2.append(max)

    output = []

    for i in range(0, len(grid)):
        output.append([])
        for j in range(0, len(grid)):
            output[i].append( (max_1[i] if max_1[i]<max_2[j] else max_2[j]) - grid[i][j])

    sum = 0

    for i in range(0, len(output)):
        for j in range(0, len(output)):
            sum+=output[i][j]

    return sum  #(max_1, max_2, sum)



print(maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
print(maxIncreaseKeepingSkyline([[59,88,44],[3,18,38],[21,26,51]]))



