class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> int:
        if matrix == []: return 0
        dp = []
        output = -float('inf')
        for r in range(len(matrix)):
            dp.append([])
            for c in range(len(matrix[0])):
                if r == 0:
                    if c == 0:
                        if matrix[r][c] == "1":
                            dp[-1].append([[1, 1]])  # [[left, above]]
                        else:
                            dp[-1].append([[0, 0]])
                    else:
                        if matrix[r][c] == "1":
                            dp[-1].append([[dp[-1][-1][-1][0] + 1, 1]])
                        else:
                            dp[-1].append([[0, 0]])
                else:
                    if c == 0:
                        if matrix[r][c] == "1":
                            dp[-1].append([[1, dp[r - 1][0][-1][1] + 1]])
                        else:
                            dp[-1].append([[0, 0]])
                    else:
                        if matrix[r][c] == "0":
                            dp[-1].append([[0, 0]])
                        else:
                            curr_left = dp[-1][-1][-1][0] + 1
                            if matrix[r - 1][c] == "0":
                                dp[-1].append([[curr_left, 1]])  # how many 1 on the left, including itself
                            else:
                                curr = []
                                for combo in dp[r - 1][c]:
                                    curr.append([min(combo[0], curr_left),
                                                 combo[1] + 1])  # follow the previous columns cnt,  but row cnt +1
                                curr.append([curr_left, 1])  # start from the current line
                                dp[-1].append(curr)

                for i in dp[-1][-1]:
                    output = max(output, i[0] * i[1])

        return output


