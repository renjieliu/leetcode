class Solution:
    def shiftGrid(self, grid: 'List[List[int]]', k: int) -> 'List[List[int]]': #O(MN | MN)
        arr = []
        for r in grid: #flatten the grid, shift k place, and form a new grid
            for c in r:
                arr.append(c)
        k %= len(arr)
        arr = (arr*2)[len(arr)-k:]
        output = []
        for r in range(len(grid)):
            output.append([])
            for c in range(len(grid[0])):
                output[-1].append(arr.pop(0))
        return output



# previous solution

# class Solution:
#     def shiftGrid(self, grid: 'List[List[int]]', k: int):
#         def shift(matrix):
#             output = matrix.copy()
#             last = []
#             for r in range(len(matrix)):
#                 last.append(matrix[r][-1])
#             final = last.pop()  # make the final element to the front of the array
#             last = [final] + last

#             for r in range(len(output)):
#                 prev = output[r][0]  # the first item of the row.
#                 output[r][0] = last.pop(0)
#                 for c in range(1, len(output[0])):
#                     if c != 0:
#                         curr = output[r][c]
#                         output[r][c] = prev  #
#                         prev = curr

#             return output

#         output = grid.copy()
#         i = 1
#         while i <= k:
#             output = shift(output)
#             i += 1

#         return output
