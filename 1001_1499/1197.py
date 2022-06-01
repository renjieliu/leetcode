class Solution:
    def minKnightMoves(self, x: int, y: int) -> int: # O( max(x, y)**2 | max(x, y)**2 )
        if x == 0 and y == 0 :
            return 0
        direction = [[-2, 1], [-2, -1], [1, 2],[1, -2], [-1, 2], [-1, -2], [2, -1], [2, 1]]
        seen = set()
        pq = [[(x**2+y**2)**0.5, 0, 0, 0]] #[distance to (x, y), count,  r, c]
        heapq.heapify(pq)
        seen.add((0, 0))
        while pq: # Dijkstra's algo,  to reach x,y, and return steps
            dis, step,  r, c = heapq.heappop(pq)
            if r == x and c == y:
                return step
            for a, b in direction:
                if (r+a, c+b) not in seen:
                    seen.add((r+a, c+b))
                    dis = ((r+a-x)**2 + (c+b-y)**2)**0.5
                    #heuristic function : total steps upto cur point + euclidean distance to target from cur point
                    heapq.heappush(pq, [step + 1 + dis, step+1, r+a, c+b])



        
# previous solution

# class Solution:
#     def minKnightMoves(self, x: int, y: int) -> int:
#         if x == y == 0:
#             return 0
#         stk = [[0, 0]]
#         move = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, -2], [-1, 2], [-2, -1], [-2, 1]]
#         lkp = {(0, 0)}
#         cnt = 0
#         while True:
#             nxt = []
#             cnt += 1
#             while stk:
#                 curr = stk.pop(0)
#                 for a, b in move:
#                     r = curr[0] + a
#                     c = curr[1] + b
#                     if r == x and c == y:
#                         return cnt
#                     if (r, c) not in lkp:
#                         nxt.append([r, c])
#                         lkp.add((r, c))
#             stk = nxt

