class Solution:
    def shortestDistance(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> int:
        start.append(0) #[r, c, distance]
        stk = [start]
        output = float('inf')
        hmp = {} #to record if current pos has been visited. if so, check if distance is less than the prev distance.. if so, add to the next iteration.
        while stk:
            nxt = []
            while stk:
                pos = stk.pop(0) #[r, c, distance]
                move = [[0,1], [0,-1], [1,0], [-1,0]]
                for a, b in move:
                    r = pos[0]
                    c = pos[1]
                    distance = pos[2]
                    while 0 <= r+a <= len(maze)-1 and 0 <= c+b <=len(maze[0])-1 and maze[r+a][c+b] == 0 :
                        r += a
                        c += b
                        distance += 1
                    if r==destination[0] and c == destination[1]:
                        output = min(output, distance)
                    elif (r,c) not in hmp or distance < hmp[(r,c)]:
                        hmp[(r,c)] = distance
                        nxt.append([r,c, distance])
            stk = nxt
        return -1 if output == float('inf') else output
