class Solution:
    def findFarmland(self, land: 'List[List[int]]') -> 'List[List[int]]':
        def dfs(output, sr, sc, land):
            direction = [[0,1],[0,-1],[1,0],[-1,0]]
            for a, b in direction:
                if -1 < sr+a < len(land)and -1 < sc+b < len(land[0]) and land[sr+a][sc+b] == 1:
                    output[-1][2]=max(output[-1][2], sr+a) # bottom right R
                    output[-1][3]=max(output[-1][3], sc+b) # bottom right C
                    land[sr+a][sc+b] = -1
                    dfs(output, sr+a, sc+b, land)
        output = []
        for r in range(len(land)):
            for c in range(len(land[0])):
                if land[r][c] == 1:
                    output.append([r,c, -float('inf'), -float('inf')]) #start_r, start_c, end_r, end_c
                    land[r][c] = -1
                    dfs(output, r, c, land)
                    if output[-1][2] == -float('inf'): #if it cannot find another 1 in the same group
                        output[-1][2] = r
                        output[-1][3] = c
        return output

