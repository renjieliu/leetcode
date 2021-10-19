class Solution:
    def gridGame(self, grid: 'List[List[int]]') -> int:
        def findPivot(grid):
            accu = [[0], [0]]
            for c in range(1, len(grid[0])):
                accu[0].append(accu[0][-1] + grid[1][c - 1])  # sum on the left of second row

            for c in range(len(grid[0]) - 1, 0, -1):  # sum on the right of the first row
                accu[1].append(accu[1][-1] + grid[0][c])
            accu[1] = accu[1][::-1]
            # print(accu)
            output = float('inf')
            for c in range(len(accu[0])):  # assuming A to pivot from here, what's score of B can get
                output = min(output, max(accu[0][c], accu[1][c]))  # left of the 2nd row or right of the 1st
            return output

        return findPivot(grid)



