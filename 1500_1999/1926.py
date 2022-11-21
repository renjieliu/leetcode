class Solution:
    def nearestExit(self, maze: 'List[List[str]]', entrance: 'List[int]') -> int: # O( MN | MN )
        visited = set()
        stk = [entrance]
        maze[entrance[0]][entrance[1]] = 'E' # mark entrance
        seen = {(entrance[0], entrance[1])}
        step = 0
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while stk: # if the stk still exists
            nxt = []
            while stk: # keep popping the stk
                r, c = stk.pop()
                for a, b in direction:
                    nxt_r = r+a 
                    nxt_c = c+b
                    if maze[r][c] != 'E' and (nxt_r in (-1, len(maze)) or nxt_c in (-1 , len(maze[0]) ) ): # current is not entrance, and next is outside
                        return step 
                    if -1 < nxt_r < len(maze) and -1 < nxt_c < len(maze[0]):
                        if maze[nxt_r][nxt_c] == '.' and (nxt_r, nxt_c) not in seen: 
                            seen.add((nxt_r, nxt_c))
                            nxt.append([nxt_r, nxt_c])
            
            step += 1 # add step after current iteration, to indicate how many steps it take to reach current point
            stk = nxt
        return -1





# previous solution

# class Solution:
#     def nearestExit(self, maze: 'List[List[str]]', entrance: 'List[int]') -> int:
#         stk = [[0, entrance[0], entrance[1]]]  # steps, r, c
#         direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
#         seen = {(entrance[0], entrance[1])}
#         output = float('inf')
#         while stk:
#             nxt = []
#             while stk:
#                 cost, sr, sc = stk.pop()
#                 for a, b in direction:
#                     if -1 < sr + a < len(maze) and -1 < sc + b < len(maze[0]) and maze[sr + a][sc + b] != "+" and (
#                     sr + a, sc + b) not in seen:
#                         if sr + a in (0, len(maze) - 1) or sc + b in (0, len(maze[0]) - 1):
#                             output = min(output, cost + 1)
#                             seen.add((sr + a, sc + b))
#                         elif (sr + a, sc + b) not in seen:
#                             seen.add((sr + a, sc + b))
#                             nxt.append([cost + 1, sr + a, sc + b])
#             stk = nxt
#             # print(stk)
#         return output if output != float('inf') else -1


