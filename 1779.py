class Solution:
    def nearestValidPoint(self, x: int, y: int, points: 'List[List[int]]') -> int:
        output=float('inf')
        curr = float('inf')
        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                if abs(p[0] -x)+ abs(p[1]-y) < curr: # no need to check =, as it needs return the smallest index
                    output = i
                    curr = abs(p[0] -x)+ abs(p[1]-y)
        return -1 if output ==float('inf') else output


