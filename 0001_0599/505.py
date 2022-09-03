class Solution:
    def shortestDistance(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> int:  # O( MN*log(MN) | MN )
        pq = [[0, start]] # to record the total path traveled
        heapq.heapify(pq)  # Dijkstra's algo, to find the shortest path to reach the destination.
        direction = [[1,0], [0,1], [-1, 0], [0, -1]]
        seen = {(start[0], start[1]): 0}
        output = float('inf')
        while pq:
            prev_dist, [prev_r, prev_c] = heapq.heappop(pq)
            if prev_r == destination[0] and prev_c == destination[1]: #prev stop at the destination 
                output = min(output, prev_dist) 
            else: 
                for a, b in direction:  # check all the 4 directions, and push the dist to the pq
                    dist = prev_dist
                    r = prev_r
                    c = prev_c
                    while -1 < r+a < len(maze) and -1 < c+b < len(maze[0]) and maze[r+a][c+b] != 1:
                        dist += 1
                        r += a 
                        c += b
                    if (r, c) not in seen or dist < seen[(r,c)]: #not seen, or current path is < than before 
                        heapq.heappush(pq, [dist, [r, c]])
                        seen[(r,c)] = dist
                
                if pq and pq[0][0] > output: #from here on, all the paths are > current output, no need to proceed the iteration
                    return output
        
        return output if output != float('inf') else -1
    

        

        

# previous solution

# class Solution:
#     def shortestDistance(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> int:
#         pq = [[0, start[0], start[1]]] #Dijkstra's algorithm, to get the shortest dist each time
#         heapq.heapify(pq) #[dist, r, c]
#         direction = [[0,1], [1,0], [0,-1] , [-1, 0]]
#         seen = {(start[0], start[1]):0}
#         output = float('inf')
#         while pq:
#             dist, sr, sc = heapq.heappop(pq)
#             if dist > output: #no need to check further, all the future dist in the pq will take more walks
#                 return output
#             for a, b in direction:
#                 r = sr
#                 c = sc
#                 walk = dist
#                 while -1< r+a < len(maze) and -1<c+b<len(maze[0]) and maze[r+a][c+b] == 0:
#                     r+=a
#                     c+=b
#                     walk+=1
#                 if r == destination[0] and c == destination[1]: # the ball stops at the destination
#                     output = min(output, walk)
#                 elif (r,c) not in seen or walk < seen[(r,c)]:
#                     heapq.heappush(pq, [walk, r, c])
#                     seen[(r,c)] = walk
#         return -1 if output == float('inf') else output



# previous approach
# class Solution:
#     def shortestDistance(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> int:
#         pq = [] #Dijkstra's Algorithm: Each time, pop out the one with min distance travelled. If it reaches the end, it's the shortest path
#         heapq.heappush(pq, [0, start[0], start[1]]) #[distance, r, c]
#         hmp = {(start[0], start[1]):0}
#         while pq:
#             nxt = []
#             direction = [[0,1], [1,0], [0,-1], [-1,0]]
#             currDist, currR, currC = heapq.heappop(pq)
#             for a, b in direction:
#                 dist = currDist
#                 r = currR
#                 c = currC
#                 while -1 < r+a < len(maze) and -1 < c + b < len(maze[0]) and maze[r+a][c+b] != 1:
#                     r+=a
#                     c+=b
#                     dist+=1
#                 if r == destination[0] and c == destination[1]:
#                     return dist
#                 elif (r,c) not in hmp or dist < hmp[(r,c)]:
#                     heapq.heappush(pq, [dist, r, c])
#                     hmp[(r,c)] = dist
#         return -1
#

# previous approach

# class Solution:
#     def shortestDistance(self, maze: 'List[List[int]]', start: 'List[int]', destination: 'List[int]') -> int:
#         start.append(0) #[r, c, distance]
#         stk = [start]
#         output = float('inf')
#         hmp = {} #to record if current pos has been visited. if so, check if distance is less than the prev distance.. if so, add to the next iteration.
#         while stk:
#             nxt = []
#             while stk:
#                 pos = stk.pop(0) #[r, c, distance]
#                 move = [[0,1], [0,-1], [1,0], [-1,0]]
#                 for a, b in move:
#                     r = pos[0]
#                     c = pos[1]
#                     distance = pos[2]
#                     while 0 <= r+a <= len(maze)-1 and 0 <= c+b <=len(maze[0])-1 and maze[r+a][c+b] == 0 :
#                         r += a
#                         c += b
#                         distance += 1
#                     if r==destination[0] and c == destination[1]:
#                         output = min(output, distance)
#                     elif (r,c) not in hmp or distance < hmp[(r,c)]:
#                         hmp[(r,c)] = distance
#                         nxt.append([r,c, distance])
#             stk = nxt
#         return -1 if output == float('inf') else output


