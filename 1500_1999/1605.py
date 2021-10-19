class Solution:
    def restoreMatrix(self, rowSum:' List[int]', colSum: 'List[int]') -> 'List[List[int]]':
        output = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        for r in range(len(rowSum)):
            for c in range(len(colSum)):
                curr = min(rowSum[r], colSum[c])
                rowSum[r] -= curr
                colSum[c] -= curr
                output[r][c] = curr
        return output


