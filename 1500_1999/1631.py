class Solution:
    def minimumEffortPath(self, heights: 'List[List[int]]') -> int: #O(m*n*logK | m*n)
        def dfs(seen, grid, r, c, cost): #O(m*n)
            direction = [[1, 0], [-1,0], [0, 1], [0, -1]]
            for a, b in direction:
                if -1< r+a < len(grid) and -1 < c+b < len(grid[0]) and (r+a, c+b) not in seen and abs(grid[r][c]-grid[r+a][c+b]) <=cost:
                    seen.add((r+a, c+b))
                    dfs(seen, grid, r+a, c+b, cost)
        
        s = 0 
        e = 10**6 
        while s <= e: #binary search to pinpoint an cost, which can be achieved.
            mid = s - (s-e)//2 
            seen = {(0,0)}
            dfs(seen, heights, 0, 0, mid)
            if (len(heights)-1, len(heights[0])-1) in seen:
                e = mid - 1 
            else:
                s = mid + 1 
        return s
    
    

# previous solution

# class Solution:
#     def minimumEffortPath(self, heights: 'List[List[int]]') -> int:
#         def dfs(check, arr,sr, sc, cost):
#             check.add((sr,sc))
#             direction = [[0,1], [1,0], [0,-1], [-1,0]]
#             for d in direction:
#                 r = sr+d[0]
#                 c = sc+d[1]
#                 if 0 <= r < len(arr) and 0 <= c < len(arr[0]) and abs(arr[r][c] - arr[sr][sc]) <= cost and (r,c) not in check:
#                     dfs(check, arr, r, c, cost)

#         s, e = 0 , max([max(r) for r in heights])
#         output = e
#         while s <= e: #to check if it can reach the end with current number
#             cost = (s + e)//2
#             check = set()
#             dfs(check, heights, 0, 0, cost)
#             if (len(heights)-1, len(heights[0])-1) in check:
#                 e = cost - 1
#                 output = cost
#             else:
#                 s= cost + 1

#         return output




