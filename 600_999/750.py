class Solution:
    def countCornerRectangles(self, grid: 'List[List[int]]') -> int:
        arr = []
        for r in range(len(grid)): #find the column of 1 in each row
            arr.append(set())
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    arr[-1].add(c)
        cnt = 0
        fact= lambda x: 1 if x in (0,1) else fact(x-1) * x
        combo = lambda n, r: fact(n)//(fact(r) * fact(n-r))
        #print(arr)
        for i in range(len(arr)): #if more than 1 column pair find a match, then it can form a rectangle
            for j in range(i+1, len(arr)):
                curr = len(arr[i] & arr[j])
                cnt += combo(curr, 2) if curr > 1 else 0
        return cnt