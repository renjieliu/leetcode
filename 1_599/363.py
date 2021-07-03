class Solution:
    def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: int) -> int:
        for r in range(len(matrix)):  # vertically add curr to next row
            for c in range(len(matrix[0]) - 1):
                matrix[r][c + 1] += matrix[r][c]

        ans = -float('inf')
        for i in range(len(matrix[0])):  # Kadane's algo, from left to right.
            for c in range(i, len(matrix[0])):
                arr = [0]
                pre = 0
                for r in range(len(matrix)):
                    pre += matrix[r][c] - (matrix[r][i - 1] if i > 0 else 0)
                    idx = bisect.bisect_left(arr, pre - k)  # find the closet number in the arr
                    if idx >= 0 and idx < len(arr):
                        ans = max(ans, pre - arr[idx])
                    bisect.insort(arr, pre)
        return ans

