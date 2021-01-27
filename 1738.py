class Solution:
    def kthLargestValue(self, matrix: 'List[List[int]]', k: int) -> int:
        dp = []
        for r in range(len(matrix)):
            dp.append([])
            for c in range(len(matrix[0])):
                if r == 0:
                    if c == 0:
                        dp[-1].append(matrix[r][c])
                    else:
                        dp[-1].append(matrix[r][c]^dp[-1][-1])
                else:
                    if c==0:
                        dp[-1].append(matrix[r][c]^dp[r-1][0])
                    else:
                        dp[-1].append(matrix[r][c]^dp[-1][-1]^dp[r-1][c]^dp[r-1][c-1]) #the left upper was xor'ed twice, need to be xor'd back

        res = []
        # print(dp)
        for r in dp:
            for c in r:
                res.append(c)
        # print(sorted(res))
        return sorted(res)[-k]
