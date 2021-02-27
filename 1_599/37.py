class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isGoodRow(arr, r, c):  # return if current row is good with current number
            cnt = 0
            for x in arr[r]:
                if x == arr[r][c]:
                    cnt += 1
            return cnt == 1

        def isGoodCol(arr, r, c):  # return if current col is good with current number
            cnt = 0
            for row in arr:
                if row[c] == arr[r][c]:
                    cnt += 1
            return cnt == 1

        def isGood9(arr, in_r, in_c):  # return if current sub box is good
            hmp = defaultdict(int)
            sr = 3 * (in_r // 3)  # gridStartingR
            sc = 3 * (in_c // 3)  # gridStartingC
            for r in range(sr, sr + 3):
                for c in range(sc, sc + 3):
                    if arr[r][c] != -1:
                        hmp[arr[r][c]] += 1
                        # if in_r == 0 and in_c == 2:
                        #     print(hmp, arr[in_r][in_c])
                        if hmp[arr[r][c]] > 1:
                            return False

            return True

        def dfs(arr, to_fill):
            if to_fill == 0:
                return 1
            else:
                for r in range(len(arr)):
                    for c in range(len(arr[0])):
                        if arr[r][c] == -1:
                            error_cnt = 0
                            for i in range(1, 10):
                                arr[r][c] = i
                                if isGoodRow(arr, r, c) and isGoodCol(arr, r, c) and isGood9(arr, r, c):
                                    if dfs(arr, to_fill - 1) == 1:  # all the rest are filled
                                        return 1
                                    else:
                                        error_cnt += 1  # the rest cannot be filled
                                else:
                                    error_cnt += 1
                            if error_cnt == 9:  # None of the number works, so need to tweak the previous numbers
                                arr[r][c] = -1  # revert the current number to -1
                                return 0

        to_fill = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = int(board[r][c]) if board[r][c] != "." else -1
                to_fill += 1 if board[r][c] == -1 else 0

        dfs(board, to_fill)
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = str(board[r][c])
        return board










