class Solution:
    def findShortestWay(self, maze: 'List[List[int]]', ball: 'List[int]', hole: 'List[int]') -> str:
        pq = [] #use the smallest instruction everytime, until reach the hole
        hmp = {(ball[0], ball[1]): ""}
        heapq.heappush(pq, [0, "",ball[0], ball[1]]) #[distance, instruction, row, col]
        output = "zzz"
        steps = float('inf')
        while pq:
            pos = heapq.heappop(pq)
            currDistance = pos[0]
            currInstruction = pos[1]
            currRow = pos[2]
            currCol = pos[3]
            direction  = {"d": [1,0], "l":[0,-1], "r":[0,1], "u":[-1,0] }
            for k, v in direction.items():
                r = currRow
                c = currCol
                distance = currDistance
                a = v[0]
                b = v[1]
                while -1 < r+a < len(maze) and -1 < c+b < len(maze[0]) and maze[r+a][c+b] == 0:
                    if r+a == hole[0] and c+b == hole[1]: #it has reach the hole
                        if distance < steps:
                            steps = distance
                            output = currInstruction + k
                        elif distance == steps:
                            output = min(output, currInstruction + k)
                        break
                    else:
                        r+=a
                        c+=b
                        distance += 1
                if r!=currRow or c!= currCol: # the ball has moved
                    if (r,c) not in hmp or currInstruction + k < hmp[(r,c)]:
                        hmp[(r,c)] = currInstruction + k
                        heapq.heappush(pq, [distance, currInstruction + k, r,c ] )

        return "impossible" if output == "zzz" else output


