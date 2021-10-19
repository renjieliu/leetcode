class Solution:
    def nearestExit(self, maze: 'List[List[str]]', entrance: 'List[int]') -> int:
        stk = [[0, entrance[0], entrance[1]]]  # steps, r, c
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        seen = {(entrance[0], entrance[1])}
        output = float('inf')
        while stk:
            nxt = []
            while stk:
                cost, sr, sc = stk.pop()
                for a, b in direction:
                    if -1 < sr + a < len(maze) and -1 < sc + b < len(maze[0]) and maze[sr + a][sc + b] != "+" and (
                    sr + a, sc + b) not in seen:
                        if sr + a in (0, len(maze) - 1) or sc + b in (0, len(maze[0]) - 1):
                            output = min(output, cost + 1)
                            seen.add((sr + a, sc + b))
                        elif (sr + a, sc + b) not in seen:
                            seen.add((sr + a, sc + b))
                            nxt.append([cost + 1, sr + a, sc + b])
            stk = nxt
            # print(stk)
        return output if output != float('inf') else -1


