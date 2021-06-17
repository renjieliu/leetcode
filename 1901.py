class Solution:
    def findPeakGrid(self, mat: 'List[List[int]]') -> 'List[int]':
        def isPeak(mat, r, c):
            up = mat[r-1][c] if r-1 >-1 else -1
            down = mat[r+1][c] if r+1 < len(mat) else -1
            left = mat[r][c-1] if c-1>-1 else -1
            right = mat[r][c+1] if c+1 < len(mat[0]) else -1
            mx = max(up, down, left, right)
            if mx == up:
                nxt_r = r-1
                nxt_c = c
            elif mx == down:
                nxt_r = r+1
                nxt_c = c
            elif mx == left:
                nxt_r = r
                nxt_c = c-1
            elif mx == right:
                nxt_r = r
                nxt_c = c+1
            return [mat[r][c] > mx , nxt_r, nxt_c]

        nxt_r = 0
        nxt_c = 0
        while True:
            check = isPeak(mat, nxt_r, nxt_c) #find the max around current, if curr is max, then return
            if check[0] == True:
                return [nxt_r, nxt_c]
            else:
                nxt_r = check[1]
                nxt_c = check[2]





