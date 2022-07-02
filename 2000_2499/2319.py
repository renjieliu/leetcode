class Solution:
    def checkXMatrix(self, grid: 'List[List[int]]') -> bool: # O( MN | 1 )
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0 and r!=c and r+c!=len(grid[0])-1: # for all non-zero, it need be on the diagonal
                    return False 
                elif grid[r][c] == 0 and (r== c or r+c == len(grid[0])-1): #none of the zero, should be on diagnoal
                    return False 
        return True

    
