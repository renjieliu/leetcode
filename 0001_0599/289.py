class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def neibours(arr, sr, sc):
            output = []
            if sr - 1 > -1:  # up
                output.append(arr[sr - 1][sc])
            if sr + 1 < len(arr):  # down
                output.append(arr[sr + 1][sc])
            if sc - 1 > -1:  # left
                output.append(arr[sr][sc - 1])
            if sc + 1 < len(arr[0]):  # right
                output.append(arr[sr][sc + 1])
            if sr - 1 > -1 and sc - 1 > -1:  # UL
                output.append(arr[sr - 1][sc - 1])
            if sr - 1 > -1 and sc + 1 < len(arr[0]):  # UR
                output.append(arr[sr - 1][sc + 1])
            if sr + 1 < len(arr) and sc - 1 > -1:  # DL
                output.append(arr[sr + 1][sc - 1])
            if sr + 1 < len(arr) and sc + 1 < len(arr[0]):  # DR
                output.append(arr[sr + 1][sc + 1])
            return output

        output = []
        for r in range(len(board)):
            output.append([])
            for c in range(len(board[0])):
                case = sum(neibours(board, r, c))
                if board[r][c] == 1:
                    if case < 2 or case > 3:
                        output[-1].append(0)
                    elif 2 <= case <= 3:
                        output[-1].append(1)
                else:
                    output[-1].append(1 if case == 3 else 0)

        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] = output[r][c]






