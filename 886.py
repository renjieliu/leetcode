class Solution:
    def possibleBipartition(self, N: int, dislikes: 'List[List[int]]') -> bool:
        if dislikes == []: return True
        hmp = {}
        for a, b in dislikes:  # build hmp for fast lookup
            if a not in hmp: hmp[a] = []
            if b not in hmp: hmp[b] = []
            hmp[a].append(b)
            hmp[b].append(a)

        pool = {}

        def dfs(hmp, pool, node, level):
            if node in pool:
                return pool[node] == level
            pool[node] = level
            if node in hmp:
                for x in hmp[node]:
                    if dfs(hmp, pool, x, (level + 1) % 2) == False:
                        return False
            return True

        for i in range(1, N + 1):
            if i not in pool:
                if dfs(hmp, pool, i, 0) == False:
                    return False
        return True

