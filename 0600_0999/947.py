class Solution:
    def removeStones(self, stones: 'List[List[int]]') -> int: # O( N | N )
        # to find how many connected islands are in the plane, the island is connected with the dots on the same col or row
        points = {(a, b) for a, b in stones}
        rows = defaultdict(lambda : [])
        cols = defaultdict(lambda : [])
        for r, c in points:
            rows[r].append(c)
            cols[c].append(r)
            
        def dfs(points, rows, cols, r, c):
            points.remove((r,c)) # remove the connected stones from the plane
            for _ in rows[r]:
                if (r, _) in points:
                    dfs(points, rows, cols, r, _)
            for _ in cols[c]:
                if (_, c) in points:
                    dfs(points, rows, cols, _, c)
    
        for r, c in stones: # check each points, and take out all the connected points
            if (r, c) in points:
                dfs(points, rows, cols, r, c)
                points.add((r,c)) # add the initial landing point back - this will be counted as an island
        
        return len(stones) - len(points)


    
