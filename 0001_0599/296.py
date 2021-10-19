class Solution:
    def minTotalDistance(self, grid: 'List[List[int]]') -> int:
        #find all the '1' position
        #sort all the 1 position row and col, to find the middle point
        #calc the dist for all the friends to travel to the meeting point

        row = []
        col  = []
        curr = -float('inf')
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row.append(r)
                    col.append(c)
        row.sort()
        col.sort()
        size = len(row)
        mid = [row[size//2], col[size//2]]

        dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        output = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    output += dist([r,c], [mid[0], mid[1]])

        return output



