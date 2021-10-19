class Solution:
    def countSubIslands(self, grid1: 'List[List[int]]', grid2: 'List[List[int]]') -> int:
        def helper(output, arr1, arr2, sr, sc):
            direction = [[0,1],[0,-1],[1,0],[-1,0]]
            for a, b in direction:
                if -1 < sr+a < len(arr2) and -1<sc+b <len(arr2[0]) and arr2[sr+a][sc+b] == 1:
                    if arr1[sr+a][sc+b] == 1:
                        arr2[sr+a][sc+b] = -1 #mark the one checked as -1
                        helper(output, arr1, arr2, sr+a, sc+b)
                    else:
                        arr2[sr+a][sc+b] = -1 #mark the one checked as -1
                        output[0] = 0 #if corresponding cell is not 1 in arr1
                        helper(output, arr1, arr2, sr+a, sc+b) #although it's the sub island, need to finish marking the remaining

        cnt = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c] == grid1[r][c] == 1:
                    output = [1]
                    helper(output, grid1, grid2, r, c)
                    cnt += output[0]
        #print(grid2)
        return cnt



