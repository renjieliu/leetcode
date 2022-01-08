class Solution:
    def removeOnes(self, grid: 'List[List[int]]') -> bool:
        def flip(arr):
            for c in range(len(arr)):
                arr[c] ^= 1 
           
        lkp = [[0 for c in range(len(grid[0]))] for r in range(len(grid))]
        change = []
        for c in range(len(grid[0])): #for the first row, flip the column to make first row same
            if grid[0][c] != 0:
                change.append(c)
        
        for c in change: #flip the cols in the lkp
            for r in range(len(lkp)):
                lkp[r][c] = 1
        
        for r in range(len(grid)): #flip rows in the lkp, to see if they can be same.
            for c in range(len(grid[0])):
                if grid[r][c] != lkp[r][c]:
                    flip(lkp[r])
                    if grid[r] != lkp[r]: #after flip, it cannot be same, return False
                        return False
                    else: # no need to check the rest of current row
                        break
                    
        return True
    
    
    
    