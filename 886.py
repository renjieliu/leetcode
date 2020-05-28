class Solution:
    def possibleBipartition(self, N: int, dislikes: 'List[List[int]]') -> bool:
        hmp = {}
        for d in dislikes:
            if d[0] not in hmp: hmp[d[0]] = []
            if d[1] not in hmp: hmp[d[1]] = []
            hmp[d[0]].append(d[1])
            hmp[d[1]].append(d[0])

        placed = {}

        def dfs(placed, hmp, n, level):
            if n in placed:
                return level == placed[n]  # to check if it's in the right place
            else:
                placed[n] = level
                if n in hmp:
                    for c in hmp[n]:
                        if dfs(placed, hmp, c, level ^ 1) == False:
                            return False
                return True

        for i in range(1, N + 1):
            if i not in placed:  # has not placed yet.
                if dfs(placed, hmp, i, 0) == False:
                    return False
        return True

