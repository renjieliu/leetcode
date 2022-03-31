class Solution:
    def maximumMinimumPath(self, grid: 'List[List[int]]') -> int: #O(mn*logk | mn)
        seen = {(0,0)}
        output=grid[0][0]
        direction = [[0,1], [1,0], [-1, 0], [0, -1]] 
        pq = [[-grid[0][0], 0,0]]
        heapq.heapify(pq)
        while pq: # go through all the neighbours of a cell, and take the largest one at each step
            v, r, c = heapq.heappop(pq)
            output = min(output, -v)
            if r==len(grid)-1 and c == len(grid[0])-1:
                return output
            for a, b in direction:
                if -1<r+a <len(grid) and -1 < c+b < len(grid[0]) and (r+a, c+b) not in seen:
                    if (r+a, c+b) not in seen:
                        heapq.heappush(pq,[-grid[r+a][c+b], r+a, c+b])
                        seen.add((r+a, c+b))

                        

# previous approach

# class Solution:
#     def maximumMinimumPath(self, grid: 'List[List[int]]') -> int:
#         output = grid[0][0]
#         direction = [[0,1],[1,0], [-1,0], [0,-1]]
#         pq = [[-grid[0][0], 0, 0]]
#         seen = {(0,0)}
#         heapq.heapify(pq)
#         while pq:
#             val, sr, sc = heapq.heappop(pq) #pop the lowest cost each time
#             output = min(output, -val)
#             if sr==len(grid)-1 and sc==len(grid[0])-1:
#                 return output
#             for a, b in direction:
#                 if -1 < sr+a < len(grid) and -1<sc+b<len(grid[0]) and (sr+a, sc+b) not in seen:
#                     seen.add((sr+a, sc+b))
#                     heapq.heappush(pq, [-grid[sr+a][sc+b], sr+a, sc+b])



