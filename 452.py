class Solution:
    def findMinArrowShots(self, points: 'List[List[int]]') -> int:
        if points == []: return 0
        points.sort(key=lambda x: x[0])
        # print(points)
        cnt = 1
        currStart = points[0][0]
        currEnd = points[0][1]
        for s, e in points[1:]:
            if currStart <= s <= currEnd:
                currEnd = min(e, currEnd)
            else:
                cnt += 1
                currStart = s
                currEnd = e
        return cnt


