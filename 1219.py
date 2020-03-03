class Solution:
    def getMaximumGold(self, grid: 'List[List[int]]') -> int:
        def find(grid, r, c , visited):
            if r >=len(grid) or c >= len(grid[0]) or c <0 or r < 0 or grid[r][c] ==0 or visited[r][c] == 1 :
                return 0
            else:
                visited[r][c] = 1
                left = find(grid, r, c-1, visited)
                right = find(grid, r, c+1, visited)
                up = find(grid, r-1, c, visited)
                down = find(grid, r+1, c, visited)
                visited[r][c] = 0
                return max(left, right, up, down)+ grid[r][c]
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        output = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] !=0:
                    output = max(output,find(grid, r, c , visited))
        return output