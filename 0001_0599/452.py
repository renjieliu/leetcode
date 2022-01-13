class Solution:
    def findMinArrowShots(self, points: 'List[List[int]]') -> int:
        points.sort()
        cnt = 1
        s = points[0][0]
        e = points[0][1] 
        for a, b in points[1:]:
            if a > e: #start a new range
                cnt += 1
                s = a 
                e = b
            else: # find the smallest overlap
                s = max(a, s) 
                e = min(b, e)
            # print(s, e)
        return cnt 



# previous approach

# class Solution:
#     def findMinArrowShots(self, points: 'List[List[int]]') -> int:
#         if points == []: return 0
#         points.sort(key=lambda x: x[0])
#         # print(points)
#         cnt = 1
#         currStart = points[0][0]
#         currEnd = points[0][1]
#         for s, e in points[1:]:
#             if currStart <= s <= currEnd:
#                 currEnd = min(e, currEnd)
#             else:
#                 cnt += 1
#                 currStart = s
#                 currEnd = e
#         return cnt


