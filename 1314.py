class Solution:
    def matrixBlockSum(self, mat: 'List[List[int]]', K: int) -> 'List[List[int]]':
        dp = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # print(dp)
        output = []
        for r in range(len(mat)):
            s = 0
            for c in range(len(mat[0])):
                s += mat[r][c]
                dp[r][c] = s

        max_r = len(mat) - 1
        max_c = len(mat[0]) - 1

        for r in range(len(mat)):
            output.append([])
            for c in range(len(mat[0])):
                lu = [max(0, r - K), max(0, c - K)]  # left upper corner , [r,c]
                ru = [max(0, r - K), min(max_c, c + K)]  # right upper, [r,c]
                ll = [min(max_r, r + K), max(0, c - K)]  # left lower, [r,c]
                rl = [min(max_r, r + K), min(max_c, c + K)]  # right lower, [r,c]
                t = 0
                row_range = [lu[0], ll[0]]
                col_range = [lu[1], ru[1]]
                for x in range(row_range[0], row_range[1] + 1):
                    t += dp[x][col_range[1]] - dp[x][col_range[0]] + mat[x][col_range[0]]
                output[-1].append(t)
        return output

