class Solution:
    def luckyNumbers(self, matrix: 'List[List[int]]') -> 'List[int]':
        minn = []
        maxx = []
        for r in range(len(matrix)):
            mi = float('inf')
            curr_mi = []
            for c in range(len(matrix[0])):
                if matrix[r][c] < mi:
                    curr_mi = [r, c]
                    mi = matrix[r][c]
            minn.append(curr_mi)

        for c in range(len(matrix[0])):
            ma = -float('inf')
            curr_ma = []
            for r in range(len(matrix)):
                if matrix[r][c] > ma:
                    curr_ma = [r, c]
                    ma = matrix[r][c]
            maxx.append(curr_ma)

        output = []
        for m in minn:
            if m in maxx:
                output.append(matrix[m[0]][m[1]])
        return output
