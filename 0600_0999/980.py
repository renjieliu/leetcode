class Solution:
    def uniquePathsIII(self, grid: 'List[List[int]]') -> int:
        def dfs(output, seen, path, total, grid, r, c):
            if grid[r][c] == 2:
                if path == total:
                    output[0] += 1 
            else:
                direction = [[0,1],[1,0], [-1,0], [0,-1]]
                for a, b in direction:
                    if -1<r+a<len(grid) and -1<c+b< len(grid[0]) and grid[r+a][c+b] not in (1, -1) and (r+a, c+b) not in seen:
                        seen.add((r+a, c+b))
                        dfs(output, seen, path+1, total, grid, r+a, c+b)
                        seen.remove((r+a, c+b))
        
        total = 0 #all the cells with 0 and 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: 
                    sr = r
                    sc = c
                elif grid[r][c] in (0,2):
                    total += 1 
        output = [0]
        dfs(output, set(), 0, total, grid, sr, sc)
        return output[0]
    
    
    
    

# previous approach
# class Solution:
#     def uniquePathsIII(self, grid: 'List[List[int]]') -> int:
#         def dfs(used, total, currWalked, r, c, grid, output):
#             # if grid[r][c] == 2: print(currWalked)
#             direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#             for d in direction:  # going thru the 4 directions
#                 tr = r + d[0]
#                 tc = c + d[1]
#                 # if tr == 2 and tc == 2 and grid[tr][tc] == 2: print(currWalked, total)
#                 if -1 < tr < len(grid) and -1 < tc < len(grid[0]) and grid[tr][tc] == 2 and currWalked == total:
#                     output[0] += 1

#                 elif -1 < tr < len(grid) and -1 < tc < len(grid[0]) and grid[tr][tc] == 0 and used[tr][
#                     tc] == 0:  # can be walked, not used
#                     used[tr][tc] = 1
#                     dfs(used, total, currWalked + 1, tr, tc, grid, output)
#                     used[tr][tc] = 0

#         total = 0
#         start, used = [], []
#         for r in range(len(grid)):
#             used.append([])
#             for c in range(len(grid[0])):
#                 used[-1].append(0)
#                 total += 1 if grid[r][c] == 0 else 0
#                 if grid[r][c] == 1:
#                     start = [r, c]
#         output = [0]
#         dfs(used, total, 0, start[0], start[1], grid, output)
#         return output[0]




