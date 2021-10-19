class Solution:
    def maximumMinimumPath(self, grid: 'List[List[int]]') -> int:
        output = grid[0][0]
        direction = [[0,1],[1,0], [-1,0], [0,-1]]
        pq = [[-grid[0][0], 0, 0]]
        seen = {(0,0)}
        heapq.heapify(pq)
        while pq:
            val, sr, sc = heapq.heappop(pq) #pop the lowest cost each time
            output = min(output, -val)
            if sr==len(grid)-1 and sc==len(grid[0])-1:
                return output
            for a, b in direction:
                if -1 < sr+a < len(grid) and -1<sc+b<len(grid[0]) and (sr+a, sc+b) not in seen:
                    seen.add((sr+a, sc+b))
                    heapq.heappush(pq, [-grid[sr+a][sc+b], sr+a, sc+b])



