class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: 'List[List[int]]') -> 'List[int]':
        hmp = {}
        for s, e in edges:
            if e not in hmp:
                hmp[e] = []
            hmp[e].append(s)  # add start to the current node

        def findRoot(hmp, node, seen, output):  # find the root of current node
            if node not in hmp:
                output.append(node)
                seen.add(node)
            else:
                for n in hmp[node]:
                    if n not in seen:
                        findRoot(hmp, n, seen, output)
                        seen.add(n)

        output = []
        seen = set()
        for i in range(n):
            if n not in seen:
                findRoot(hmp, i, seen, output)
        return list(set(output))


