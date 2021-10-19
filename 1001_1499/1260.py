class Solution:
    def shiftGrid(self, grid: 'List[List[int]]', k: int):
        def shift(matrix):
            output = matrix.copy()
            last = []
            for r in range(len(matrix)):
                last.append(matrix[r][-1])
            final = last.pop()  # make the final element to the front of the array
            last = [final] + last

            for r in range(len(output)):
                prev = output[r][0]  # the first item of the row.
                output[r][0] = last.pop(0)
                for c in range(1, len(output[0])):
                    if c != 0:
                        curr = output[r][c]
                        output[r][c] = prev  #
                        prev = curr

            return output

        output = grid.copy()
        i = 1
        while i <= k:
            output = shift(output)
            i += 1

        return output
