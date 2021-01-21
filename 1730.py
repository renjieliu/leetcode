class Solution:
    def getFood(self, grid: 'List[List[str]]') -> int:
        food = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "#":
                    food.append([r,c])

        step = 0
        while food:
            step += 1
            nxt_food = [] #will treat as food is in the next cell, and iterate till find the person.
            for r, c in food:
                for d in [[1,0],[0,-1],[-1,0], [0,1]]:
                    if 0 <= r+d[0] < len(grid) and 0 <= c+d[1]< len(grid[0]):
                        if grid[r+d[0]][c+d[1]] == "*":
                            return step
                        elif grid[r+d[0]][c+d[1]] == "O":
                            grid[r+d[0]][c+d[1]] = "!"
                            nxt_food.append([r+d[0], c+d[1]])
            food = nxt_food
        return -1

