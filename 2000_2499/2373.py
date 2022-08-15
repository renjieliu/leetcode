class Solution:
    def largestLocal(self, grid: 'List[List[int]]') -> 'List[List[int]]': # O( N**3 | N )  N = len(grid)
        def helper(matrix): # get the max for current matrix
            return max([max(_) for _ in matrix])
        output = []
        for r in range(2, len(grid)): # brutal force to get the max for each 3*3 matrix
            output.append([])
            for c in range(2, len(grid[0])):
                output[-1].append( helper([_[c-2: c+1] for _ in grid[r-2: r+1]]))
        return output
    
    
    
