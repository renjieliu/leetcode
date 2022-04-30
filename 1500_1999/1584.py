class Solution:
    def minCostConnectPoints(self, points: 'List[List[int]]') -> int: # O(n2 * logN | n2)
        def find(root, v): # to find the root of v
            if root[v] != v:
                root[v] = find(root, root[v])
            return root[v]
        
        def union(root, size, v1, v2): #union the 2 nodes, move the smaller to the larger
            r_v1 = find(root, v1)
            r_v2 = find(root, v2)
            if r_v1 != r_v2:
                if size[r_v1] >= size[r_v2]:
                    root[r_v2] = r_v1
                    size[r_v1] += 1
                elif size[r_v2] > size[r_v1]:
                    root[r_v1] = r_v2
                    size[r_v2] += 1
        
        
        if len(points) == 1 :
            return 0
        cnt = 0  
        output = 0
        root = [_ for _ in range(len(points))] 
        size = [0 for _ in range(len(points))]
        manhattan = lambda a, b: abs(a[0]-b[0]) + abs(a[1] - b[1])
        dist = []
        for i in range(len(points)): #Kruskal's algo to connect all the nodes
            for j in range(i+1, len(points)):
                dist.append([i, j, manhattan(points[i], points[j])])
        
        dist.sort(key = lambda x: x[2])
        
        for a, b, d in dist:
            if find(root, a) != find(root, b):
                cnt += 1 
                output += d
                union(root, size, a, b) 
                if cnt == len(points)-1:
                    return output

                
             

# previous solution

# class Solution:
#     def minCostConnectPoints(self, points: 'List[List[int]]') -> int:
#         dist = lambda a,b: abs(a[0] -b[0]) + abs(a[1]-b[1])
#         arr = []
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 arr.append([i,j, dist(points[i], points[j])])
#         arr.sort(key=lambda x: x[2])
#         root = [_ for _ in range(len(points))]
#         output = 0
#         for p1, p2, cost in arr:
#             if root[p1] != root[p2]:
#                 prev = root[p2]
#                 curr = root[p1]
#                 root[p2] = curr
#                 output += cost
#                 for p in range(len(points)):
#                     if root[p] == prev:
#                         root[p] = curr
#         return output



# previous approach
# class Solution:
#     def minCostConnectPoints(self, points: 'List[List[int]]') -> int:
#         arr = [] #kruscal's algorithm
#         dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1]- b[1]) # to calcualate the Manhattan distance of 2 points
#         for i in range(len(points)):
#             for j in range(i+1, len(points)):
#                 arr.append([i, j, dist(points[i], points[j])])
#         arr.sort(key = lambda x : x[2]) #the lowest distance will be considered first
#         root = [_ for _ in range(len(points))]
#         output = 0
#         for p1, p2, cost in arr:
#             if root[p1] != root[p2]:
#                 output += cost
#                 prev = root[p2]
#                 curr = root[p1]
#                 for i in range(len(root)):
#                     if root[i] == prev:
#                         root[i] = curr
#         return output