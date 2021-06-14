class Solution:
    def minCostConnectPoints(self, points: 'List[List[int]]') -> int:
        dist = lambda a,b: abs(a[0] -b[0]) + abs(a[1]-b[1])
        arr = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                arr.append([i,j, dist(points[i], points[j])])
        arr.sort(key=lambda x: x[2])
        root = [_ for _ in range(len(points))]
        output = 0
        for p1, p2, cost in arr:
            if root[p1] != root[p2]:
                prev = root[p2]
                curr = root[p1]
                root[p2] = curr
                output += cost
                for p in range(len(points)):
                    if root[p] == prev:
                        root[p] = curr
        return output



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