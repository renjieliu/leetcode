class Solution:
    def getFood(self, grid: 'List[List[str]]') -> int:
        # find the person, and bfs to approach the food
        direction = [[0,1], [1,0], [-1,0], [0,-1]]
        total_r = len(grid)
        total_c = len(grid[0])
        for r in range(total_r):
            for c in range(total_c):
                if grid[r][c] == "*":
                    person =[[r,c]]
                    break
        step = 0
        while person:
            nxt_position = []
            step += 1
            for pr, pc in person:
                for dr, dc in direction: #the next possible positions
                    r = pr+dr
                    c = pc+dc
                    if 0 <= r < total_r and 0 <= c < total_c:
                        if grid[r][c]=="#":
                            return step
                        elif grid[r][c] == "O":
                            grid[r][c] = "Taken"
                            nxt_position.append([r,c])
            person = nxt_position

        return -1


# previous approach
# class Solution:
#     def getFood(self, grid: 'List[List[str]]') -> int:
#         people = []
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == "*":
#                     people.append([r,c])
#                     break #there's only person in the grid
#         step = 0
#         valid = lambda grid, r, c: True if 0 <= r < len(grid) and 0 <= c < len(grid[0]) else False
#         while people: # from person location to reach the food
#             step +=1
#             next_position = [] #the next position the person can be standing at
#             for sr, sc in people:
#                 for d in [[1,0],[0,-1],[-1,0], [0,1]]:
#                     r = sr + d[0]
#                     c = sc + d[1]
#                     if valid(grid, r,c):
#                         if grid[r][c] == "#" :
#                             return step
#                         elif grid[r][c] == "O":
#                             next_position.append([r,c])
#                             grid[r][c] = "walked"
#             people = next_position
#
#         return -1

# previous approach
# class Solution:
#     def getFood(self, grid: 'List[List[str]]') -> int:
#         food = []
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == "#":
#                     food.append([r,c])
#
#         step = 0
#         while food:
#             step += 1
#             nxt_food = [] #will treat as food is in the next cell, and iterate till find the person.
#             for r, c in food:
#                 for d in [[1,0],[0,-1],[-1,0], [0,1]]:
#                     if 0 <= r+d[0] < len(grid) and 0 <= c+d[1]< len(grid[0]):
#                         if grid[r+d[0]][c+d[1]] == "*":
#                             return step
#                         elif grid[r+d[0]][c+d[1]] == "O":
#                             grid[r+d[0]][c+d[1]] = "!"
#                             nxt_food.append([r+d[0], c+d[1]])
#             food = nxt_food
#         return -1
#
