class Solution:
    def maxMatrixSum(self, matrix: 'List[List[int]]') -> int:
        deduct = float('inf')
        total = 0
        neg_cnt = 0  # if even number of neg, they can be flipped to pos. If odd, total - 2*min(abs(value))
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] < 0:
                    neg_cnt += 1
                total += abs(matrix[r][c])
                deduct = matrix[r][c] if abs(matrix[r][c]) < abs(deduct) else deduct
        return total - (0 if neg_cnt % 2 == 0 else 2 * abs(deduct))

