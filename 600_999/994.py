class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> int:
        cnt_fresh = 0
        entry = [[]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    entry[-1].append([r, c])
                elif grid[r][c] == 1:
                    cnt_fresh += 1
        if cnt_fresh == 0:
            return 0
        else:
            minutes = 0
            check = [[None for c in range(len(grid[0]))] for r in range(len(grid))]
            while entry:
                e = entry.pop(0)  # current rotten layer
                if len(e) == 0:
                    break
                else:
                    affect = 0
                    entry.append([])
                    while e:  # for current point
                        b = e.pop(0)
                        for d in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                            curr_r = b[0] + d[0]
                            curr_c = b[1] + d[1]
                            if -1 < curr_r < len(grid) and -1 < curr_c < len(grid[0]) and grid[curr_r][curr_c] == 1 and \
                                    check[curr_r][curr_c] == None:
                                check[curr_r][curr_c] = 1
                                cnt_fresh -= 1
                                affect += 1
                                entry[-1].append([curr_r, curr_c])
                    if affect != 0:
                        minutes += 1

            return -1 if cnt_fresh > 0 else minutes
