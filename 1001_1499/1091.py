class Solution:
    def shortestPathBinaryMatrix(self, grid: 'List[List[int]]') -> int: # O(N2 | N2)
        if grid[0][0] != 0: return -1
        direction = []
        for i in (-1, 0, 1): # to generate the 8 directional directions
            for j in (-1, 0, 1):
                if i!=0 or j != 0: #avoid moving the [0, 0] direction
                    direction.append([i,j])
        # print(direction)
        stk = [[0,0]]
        seen = {(0,0)}
        step = 0 
        while stk: # BFS to search for the 0 in the adjacent cells, and move from there.
            nxt = []
            step += 1
            while stk:
                r, c = stk.pop()
                if r == len(grid)-1 and c == len(grid[0])-1: # reached the bottom right corner 
                    return step
                for a , b in direction:
                    nxt_r = r+a
                    nxt_c = c+b
                    if -1 < nxt_r < len(grid) and -1 < nxt_c < len(grid[0]) and grid[nxt_r][nxt_c] == 0 and (nxt_r, nxt_c) not in seen:
                        nxt.append([nxt_r, nxt_c])
                        seen.add((nxt_r, nxt_c))
        
            stk = nxt
        
        return -1
    

               
# previous solution 

# class Solution:
#     def shortestPathBinaryMatrix(self, grid: 'List[List[int]]') -> int:
#         if grid[0][0] != 0 or grid[-1][-1] != 0:
#             return -1
#         elif len(grid) == 1:  # only one element in the grid and it's 0, no need to walk
#             return 1
#         else:
#             arr = [[0, 0]]
#             cnt = 1
#             while arr:  # BFS to check all the possibilities
#                 cnt += 1
#                 nxt = []
#                 direction = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
#                 for sr, sc in arr:
#                     for x, y in direction:
#                         r = sr + x
#                         c = sc + y
#                         if r == len(grid) - 1 and c == len(grid[0]) - 1 and grid[r][c] == 0:
#                             return cnt
#                         elif 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
#                             nxt.append([r, c])
#                             grid[r][c] = 1
#                 arr = nxt

#             return -1






