class Solution:
    def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: int) -> int:
        ans = -float('inf')
        for control in range(len(matrix[0])):
            kadane = [0] * len(matrix)
            for c in range(control, len(matrix[0])):
                curr = 0
                maxKadane = -float('inf')
                for r in range(len(matrix)):
                    kadane[r] += matrix[r][c]
                    curr = max(curr + kadane[r], kadane[r])
                    maxKadane = max(maxKadane, curr)

                if maxKadane <= k:  # if the ans is <= than k, we do not need the binary search
                    ans = max(maxKadane, ans)

                else:
                    # find the largest sum of a subarray which is no more than K
                    arr = [0]
                    total, localMax = 0, -float('inf')
                    for item in kadane:  # accumulate the sum and find the segment closest to the K
                        total += item
                        overflow = total - k
                        # find the accumulated range, which is the most closest to the overflow
                        rangeStart = bisect.bisect_left(arr, overflow)
                        if rangeStart < len(arr):  # if rangeStart == len(arr), meaning the arr keep increasing.
                            rangeSum = total - arr[rangeStart]  # the range
                            localMax = max(localMax, rangeSum)
                        bisect.insort(arr, total)
                    ans = max(ans, localMax)
        return ans


# previous copied approach
# class Solution:
#     def maxSumSubmatrix(self, matrix: 'List[List[int]]', k: int) -> int:
#         for r in range(len(matrix)):  # vertically add curr to next row
#             for c in range(len(matrix[0]) - 1):
#                 matrix[r][c + 1] += matrix[r][c]
#
#         ans = -float('inf')
#         for i in range(len(matrix[0])):  # Kadane's algo, from left to right.
#             for c in range(i, len(matrix[0])):
#                 arr = [0]
#                 pre = 0
#                 for r in range(len(matrix)):
#                     pre += matrix[r][c] - (matrix[r][i - 1] if i > 0 else 0)
#                     idx = bisect.bisect_left(arr, pre - k)  # find the closet number in the arr
#                     if idx >= 0 and idx < len(arr):
#                         ans = max(ans, pre - arr[idx])
#                     bisect.insort(arr, pre)
#         return ans

