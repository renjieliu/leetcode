class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> int:
        def helper(hmp, arr, r, c ):
            if (r,c) in hmp:
                return hmp[(r,c)]
            else:
                if r == len(arr)-1:
                    hmp[(r,c)] = arr[r][c]
                else:
                    A = arr[r][c] + helper(hmp, arr, r+1, c)
                    B = arr[r][c] + helper(hmp, arr, r+1, c+1)
                    hmp[(r,c)] = min(A,B)
                return hmp[(r,c)]
        hmp = {}
        helper(hmp, triangle, 0, 0)
        return hmp[(0,0)]


