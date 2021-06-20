class Solution:
    def swimInWater(self, grid: 'List[List[int]]') -> int:
        seen = set((0, 0))
        pq = [(0, 0, 0)]  # [t, r, c] ,  everytime,pick the one start the earliest...
        heapq.heapify(pq)
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        output = grid[0][0]
        while pq:
            t, sr, sc = heapq.heappop(pq)
            output = max(t, output)
            for a, b in direction:
                r = sr
                c = sc
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return output
                while -1 < r + a < len(grid) and -1 < c + b < len(grid[0]):
                    if (r + a, c + b) not in seen:
                        heapq.heappush(pq, (grid[r + a][c + b], r + a, c + b))
                        seen.add((r, c))
                    break



