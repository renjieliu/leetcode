class Solution:
    def minimumEffortPath(self, heights: 'List[List[int]]') -> int:
        def dfs(check, arr,sr, sc, cost):
            check.add((sr,sc))
            direction = [[0,1], [1,0], [0,-1], [-1,0]]
            for d in direction:
                r = sr+d[0]
                c = sc+d[1]
                if 0 <= r < len(arr) and 0 <= c < len(arr[0]) and abs(arr[r][c] - arr[sr][sc]) <= cost and (r,c) not in check:
                    dfs(check, arr, r, c, cost)

        s, e = 0 , max([max(r) for r in heights])
        output = e
        while s <= e: #to check if it can reach the end with current number
            cost = (s + e)//2
            check = set()
            dfs(check, heights, 0, 0, cost)
            if (len(heights)-1, len(heights[0])-1) in check:
                e = cost - 1
                output = cost
            else:
                s= cost + 1

        return output