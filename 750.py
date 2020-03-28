class Solution:
    def countCornerRectangles(self, grid: 'List[List[int]]') -> int:
        def one_loc(arr):  # to find all the combination of the 1 loc of the curr row
            output = []
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    output.append((arr[i], arr[j]))
            return output

        pool = {}
        if len(grid) < 2:
            return 0
        else:
            for r in range(len(grid)):
                arr = []  # the location of 1
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        arr.append(c)
                if len(arr) > 1:
                    for loc in one_loc(arr):
                        if loc not in pool:
                            pool[loc] = 0
                        pool[loc] += 1
            fact = lambda x: 1 if x <= 1 else x * fact(x - 1)
            output = 0
            for v in pool.values():
                if v >= 2:
                    output += fact(v) // (fact(v - 2) * fact(2))
            return output



