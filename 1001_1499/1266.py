class Solution:
    def minTimeToVisitAllPoints(self, points: 'List[List[int]]') -> int:
        def distance (p1, p2):
            diffX = abs(p1[0]-p2[0])
            diffY = abs(p1[1] - p2[1])
            diag = min(diffX,diffY) #walk diag first and walk the rest
            rest = max(diffX-diag, diffY-diag) #at least one of those 2 will be 0. and we can walk the rest.
            return diag+rest

        if len(points) ==1:
            return 0
        else:
            i = 1
            t = 0
            while i < len(points):
                t+=distance(points[i], points[i-1])
                i+=1
            return t
