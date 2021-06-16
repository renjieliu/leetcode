class Solution:
    def regionsBySlashes(self, grid: 'List[str]') -> int:
        #expanding the grid by 3*3, mark the line as 1, and count islands
        arr = [[0 for _ in range(3*len(grid[0]))] for _ in range(3*len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "\\":
                    arr[r*3][c*3] = 1
                    arr[r*3+1][c*3+1] = 1
                    arr[r*3+2][c*3+2] = 1
                elif grid[r][c] == "/":
                    arr[r*3][c*3+2] = 1
                    arr[r*3+1][c*3+1] = 1
                    arr[r*3+2][c*3] = 1

        def clearSameIsland(arr, sr, sc): # this is to clear current island
            direction = [[1,0], [-1,0],[0,-1],[0,1]]
            for a , b in direction:
                if -1 < sr+a < len(arr) and -1 < sc+b < len(arr[0]) and arr[sr+a][sc+b] == 0:
                    arr[sr+a][sc+b] = 1
                    clearSameIsland(arr,sr+a, sc+b )

        cnt = 0
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                if arr[r][c] == 0: # island has not been cleared...
                    cnt += 1
                    arr[r][c] = 1
                    clearSameIsland(arr, r, c)
        return cnt


