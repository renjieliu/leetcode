class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if matrix == []: return []
        output = []
        r, c = 0, 0
        cnt = 0
        while cnt < len(matrix) + len(matrix[0]):
            curr = []
            r = cnt if cnt <= len(matrix) - 1 else len(matrix) - 1
            c = 0 if cnt <= len(matrix) - 1 else cnt - (len(matrix) - 1)
            while r > -1 and c < len(matrix[0]):
                curr.append(matrix[r][c])
                r -= 1
                c += 1

            if cnt % 2 == 0:
                for c in curr:
                    output.append(c)
            else:
                for c in curr[::-1]:
                    output.append(c)
            cnt += 1
        return output