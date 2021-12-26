class Solution:
    def kClosest(self, points: 'List[List[int]]', k: int) -> 'List[List[int]]': #no need to consider multiple points with same distance, as stated from the question description, the result is unique.
        return sorted(points, key=lambda x: (x[0]**2 + x[1]**2)**0.5)[:k]
    
   


# previous approach
# class Solution:
#     def kClosest(self, points: 'List[List[int]]', K: int) -> 'List[List[int]]':
#         dist = lambda x, y: ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
#         hmp = {}
#         origin = [0, 0]
#         for p in points:
#             d = dist(origin, p)
#             if d not in hmp:
#                 hmp[d] = []
#             hmp[d].append(p)
#         sortedKey = sorted(hmp.keys())
#         output = {}
#         for k in sortedKey:
#             if len(output) < K:
#                 while hmp[k]:
#                     output[tuple(hmp[k].pop())] = None
#         return list(output.keys())




#OLD solution - it seems not considering the cases where the same distance has multiple points - although it passes all the test cases
# def kClosest(points: 'List[List[int]]', K: 'int'):
#     dic = {}
#     distance  = []
#     for i in points:
#         dic[(i[0]**2 + i[1]**2 )**0.5 ] = i #use the distance as  key
#         distance.append((i[0]**2 + i[1]**2 )**0.5 ) #push the value to a list
#
#     distance.sort()
#     pick = distance[:K] #get the first K points
#
#     output = []
#
#     for i in pick:
#         output.append(dic[i]) #lookup the distance in the hash, and get the point out.
#
#     return output
#
# print(kClosest([[3,3],[5,-1],[-2,4]], 2))


