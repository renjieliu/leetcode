class Solution:
    def maxWidthOfVerticalArea(self, points: 'List[List[int]]') -> int:
        points.sort(key = lambda x: x[0])
        output = -float('inf')
        for i in range(1, len(points)):
            output = max(output, points[i][0] - points[i-1][0])
        return output