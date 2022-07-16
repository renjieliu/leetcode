class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> int: # O( MN | 1)
        def helper(curr, r, c, grid): #dfs to count all the 1's from r and c.
            direction = [[1,0], [0,-1], [-1,0], [0,1]]
            for a, b in direction:
                if -1 < r+a < len(grid) and -1 < c+b < len(grid[0]) and grid[r+a][c+b] == 1:
                    grid[r+a][c+b] = 0 
                    curr[0] += 1
                    helper(curr, r+a, c+b, grid)
        
        output = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0 
                    curr = [1] #to record the area of current 1's 
                    helper(curr, r, c, grid)
                    output = max(output, curr[0])
        
        return output



# previous solution

# class Solution:
#     def maxAreaOfIsland(self, grid: 'List[List[int]]') -> int:
#         def dfs(output,arr, sr, sc):
#             output[-1]+=1
#             arr[sr][sc] = 0
#             directions = [[0,1], [-1,0], [0,-1], [1,0]]
#             for a , b in directions:
#                 r = sr+a
#                 c = sc+b
#                 if -1<r<len(arr) and -1<c<len(arr[0]) and arr[r][c]==1:
#                     dfs(output, arr, r, c)

#         output = []
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 1:
#                     print(r,c )
#                     output.append(0)
#                     dfs(output, grid, r, c)
#         # print(output)
#         return max(output) if output else 0


# previous approach
# def dfs(done, grid, sr, sc, val, currMax):
#     if done[sr][sc] == None and grid[sr][sc] == 1:
#         done[sr][sc] = 1
#         currMax.append(1)
#         # up
#         for r in range(sr - 1, -1, -1):
#             if dfs(done, grid, r, sc, val + 1,  currMax) == -1:
#                 break
#
#         # down
#         for r in range(sr + 1, len(grid)):
#             if dfs(done, grid, r, sc, val + 1,  currMax) == -1:
#                 break
#         # left
#         for c in range(sc - 1, -1, -1):
#             if dfs(done, grid, sr, c, val + 1,  currMax) == -1:
#                 break
#
#         # right
#         for c in range(sc + 1, len(grid[0])):
#             if dfs(done, grid, sr, c, val + 1,  currMax) == -1:
#                 break
#     else:
#         return -1
#
#
# def maxAreaOfIsland(grid: 'List[List[int]]'):
#     done = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     res = 0
#     for r in range(len(grid)):
#         for c in range(len(grid[0])):
#             if done[r][c] == None and grid[r][c] == 1:
#                 currMax = []
#                 dfs(done, grid, r, c, 1, currMax)
#                 res = max(res, len(currMax))
#
#     return res
#
#
# print(maxAreaOfIsland(
#     [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
