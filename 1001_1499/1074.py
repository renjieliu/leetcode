class Solution:
    def numSubmatrixSumTarget(self, matrix: 'List[List[int]]', target: int) -> int: # O(R**2*C | RC )
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)] # prefix sum up to current cell
        for r in range(1, len(matrix)+1):
            for c in range(1, len(matrix[0])+1):
                dp[r][c] = dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1] + matrix[r-1][c-1] 
        count = 0
        for r in range(1, len(matrix)+1):
            for r1 in range(r, len(matrix)+1):
                hmp = defaultdict(lambda: 0) 
                hmp[0] = 1
                for c in range(1, len(matrix[0])+1):
                    curr = dp[r1][c] - dp[r-1][c] #sum of current matrix 
                    count += hmp[curr-target] #curr is the prefix total, curr-target = k, if k was seen before, the matrix in between is the one we are looking for .
                    hmp[curr] += 1
        return count
    
    


# previous solution

# class Solution:
#     def numSubmatrixSumTarget(self, matrix: 'List[List[int]]', target: int) -> int: # O(R**2*C | RC )
#         dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)] # prefix sum up to current cell
#         for r in range(1, len(matrix)+1):
#             for c in range(1, len(matrix[0])+1):
#                 dp[r][c] = dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1] + matrix[r-1][c-1] 
#         count = 0
#         for r in range(1, len(matrix)+1):
#             for r1 in range(r, len(matrix)+1):
#                 hmp = defaultdict(lambda: 0) 
#                 hmp[0] = 1
#                 for c in range(1, len(matrix[0])+1):
#                     curr = dp[r1][c] - dp[r-1][c] #sum of current matrix 
#                     count += hmp[curr-target] #curr is the prefix total, curr-target = k, if k was seen before, the matrix in between is the one we are looking for .
#                     hmp[curr] += 1
#         return count
    
    


# previous solution

# class Solution:
#     def numSubmatrixSumTarget(self, matrix: 'List[List[int]]', target: int) -> int:
#         r, c = len(matrix), len(matrix[0])

#         # compute 2D prefix sum
#         ps = [[0] * (c + 1) for _ in range(r + 1)]
#         for i in range(1, r + 1):
#             for j in range(1, c + 1):
#                 ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + matrix[i - 1][j - 1]

#         count = 0
#         # reduce 2D problem to 1D one
#         # by fixing two rows r1 and r2 and
#         # computing 1D prefix sum for all matrices using [r1..r2] rows
#         for r1 in range(1, r + 1):
#             for r2 in range(r1, r + 1):
#                 h = defaultdict(int)
#                 h[0] = 1

#                 for col in range(1, c + 1):
#                     # current 1D prefix sum
#                     curr_sum = ps[r2][col] - ps[r1 - 1][col]

#                     # add subarrays which sum up to (curr_sum - target)
#                     count += h[curr_sum - target]

#                     # save current prefix sum
#                     h[curr_sum] += 1

#         return count



