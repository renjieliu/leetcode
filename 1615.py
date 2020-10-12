class Solution:
    def maximalNetworkRank(self, n: int, roads: 'List[List[int]]') -> int:
        if roads == []: return 0
        hmp = {}
        for s, e in roads:
            if s not in hmp:
                hmp[s] = set()
            hmp[s].add(e)
            if e not in hmp:
                hmp[e] = set()
            hmp[e].add(s)

        output = 0
        for i in range(n):  # check each node
            if i in hmp:
                curr = len(hmp[i])  # node connected to it
                for j in range(i + 1, n):  # check other nodes
                    if j in hmp:
                        nodes = len(hmp[j]) - (
                            1 if i in hmp[j] else 0)  # nodes connected minus 1 if connect to the original nodes.
                        output = max(output, curr + nodes)
        return output




