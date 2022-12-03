class Solution:
    def onesMinusZeros(self, grid: 'List[List[int]]') -> 'List[List[int]]': # O( MN | MN )
        hmp_r_1 = defaultdict(lambda: 0)
        hmp_c_1 = defaultdict(lambda: 0)
        hmp_r_0 = defaultdict(lambda: 0)
        hmp_c_0 = defaultdict(lambda: 0)
        for r in range(len(grid)): # record 0 and 1 statistics for each row and col
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    hmp_r_0[r] += 1
                    hmp_c_0[c] += 1 
                else:
                    hmp_r_1[r] += 1
                    hmp_c_1[c] += 1 
        diff = []
        for r in range(len(grid)):
            diff.append([])
            for c in range(len(grid[0])):
                curr = hmp_r_1[r] + hmp_c_1[c] - hmp_r_0[r] - hmp_c_0[c] # compute the diff[i][j]
                diff[-1].append(curr)
        
        return diff
    


    
