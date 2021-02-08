class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':
        def good(arr, row, col, n):  # if placed current queen at row, col, check if it's valid per previous row setup
            if arr == []: return 1
            for r in range(row):
                if arr[r][col] == 1:  # check if exists on the same col
                    return 0
                gap = row - r
                if row - gap >= 0 and col - gap >= 0 and arr[row - gap][col - gap] == 1:  # check the left above diag
                    return 0
                if row - gap >= 0 and col + gap < n and arr[row - gap][col + gap] == 1:  # check the right above diag
                    return 0
            return 1

        def helper(output, arr, r, c, n, curr):
            if curr == n:
                output.append([])
                for r in arr:
                    output[-1].append("")
                    for c in r:
                        output[-1][-1] += ("Q" if c else ".")
            else:
                for r in range(r, n):
                    for c in range(n):
                        if good(arr[:r], r, c, n) == 1:  # if it can be placed here
                            arr[r][c] = 1
                            helper(output, arr, r + 1, c, n, curr + 1)
                            arr[r][c] = 0

        arr = [[0 for _ in range(n)] for _ in range(n)]
        output = []
        helper(output, arr, 0, 0, n, 0)
        return output





