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

        def dfs(node, c):
            if node in pool:
                return pool[node] == c
            pool[node] = c
            if node in hmp:
                for x in hmp[node]:
                    if dfs(x, c ^ 1) == False:
                        return False
            return True

        for node in range(1, N + 1):
            if node not in pool:
                if dfs(node, 0) == False:
                    return False
        return True
