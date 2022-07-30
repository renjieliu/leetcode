class Solution:
    def equalPairs(self, grid: 'List[List[int]]') -> int: # O( MN | MN )
        rows = defaultdict(lambda: 0) #count all the row occurrence in the map
        for g in grid:
            rows[tuple(g)] += 1 
        
        cols = defaultdict(lambda: 0) # count all the col occurrence in the map
        for c in range(len(grid[0])): 
            curr = []
            for r in range(len(grid)):
                curr.append(grid[r][c])
            cols[tuple(curr)] += 1 
    
        output = 0
        for k, v in rows.items(): # calc the pairs
            if k in cols:
                output += v * cols[k]
        return output 
    
    

