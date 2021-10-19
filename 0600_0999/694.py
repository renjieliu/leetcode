class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> int:
        lkp = []
        cnt = 0
        for r in range(len(grid)): #give id each cell
            lkp.append([])
            for c in range(len(grid[0])):
                lkp[-1].append(cnt)
                cnt+=1
        def dfs(sr, sc, grid, output, lkp): # find all the islands in the grid, pick up the id
            direction = [[0,1],[1,0],[0,-1], [-1,0]]
            for d in direction:
                r = sr+d[0]
                c = sc+d[1]
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                    output[-1].append(lkp[r][c])
                    grid[r][c] = 0
                    dfs(r,c, grid, output, lkp)
        output = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    output.append([lkp[r][c]])
                    dfs(r, c, grid, output, lkp)

        res = set()
        for island in output: #for each island, check the distance b/w nodes. same islands should have same distance
            island.sort()
            #print(island)
            if len(island) == 1:
                res.add(tuple([-1]))
            else:
                x = [i%len(grid[0]) for i in island] #place each node as if it's on the first row
                #print('x', x)
                t = []
                for i in range(1, len(x)):
                    t.append(x[i] - x[i-1])
                res.add(tuple(t))
        #print(res)
        return len(res)









