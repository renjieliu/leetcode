class Solution:
    def findBall(self, grid: 'List[List[int]]') -> 'List[int]': # O( MN | N ), M = len(grid), N = len(grid[0])
        output = [] 
        for i in range(len(grid[0])): # check each ball from the first row
            r = 0 
            c = i
            good = 1 
            while r < len(grid):
                if grid[r][c] == 1:
                    if c == len(grid[0])-1 or grid[r][c+1] == -1 : # the rightmost col or the nxtcol is -1 
                        output.append(-1) 
                        break
                    else:
                        r += 1 # move to the next row 
                        c += 1
                elif grid[r][c] == -1:
                    if c == 0 or grid[r][c-1] == 1: # the leftmost col or prev col is 1
                        output.append(-1)
                        break
                    else:
                        r += 1 # move to the next row 
                        c -= 1
            
            if r == len(grid):
                output.append(c)

        return output
                
