class Solution:
    def rotateGrid(self, grid: 'List[List[int]]', k: int) -> 'List[List[int]]':
        def peel(grid, n):
            output = []
            r = n
            for c in range(n, len(grid[0])-n-1):
                output.append(grid[r][c])

            c = len(grid[0])-1-n
            for r in range(n, len(grid)-1-n):
                output.append(grid[r][c])

            r = len(grid)-1-n
            for c in range(len(grid[0])-n-1, n, -1):
                output.append(grid[r][c])

            c = n
            for r in range(len(grid)-n-1, n, -1):
                output.append(grid[r][c])
            return output

        def putBack(grid, arr, n):
            r = n
            for c in range(n, len(grid[0])-n-1):
                grid[r][c] = arr.pop(0)
            c = len(grid[0])-1-n
            for r in range(n, len(grid)-1-n):
                grid[r][c] = arr.pop(0)
            r = len(grid)-1-n
            for c in range(len(grid[0])-n-1, n, -1):
                grid[r][c] = arr.pop(0)
            c = n
            for r in range(len(grid)-n-1, n, -1):
                grid[r][c] = arr.pop(0)

        def shift(arr, k):
            n = k % len(arr) #the real shift times
            if n == 0 :
                return arr
            else:
                return arr[-(len(arr)-n):] + arr[:n]

        totalLayer = min(len(grid), len(grid[0]))//2
        flat = []
        for i in range(totalLayer):
            flat.append(peel(grid, i))
        #print(flat)
        cooked = []
        for f in flat: #shift each layer
            cooked.append(shift(f, k))

        for n in range(len(cooked)): #put the arr back to the grid
            putBack(grid, cooked[n], n)
        return grid



