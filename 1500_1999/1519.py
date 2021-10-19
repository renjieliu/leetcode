class Solution:
    def countSubTrees(self, n: int, edges: 'List[List[int]]', labels: str) -> 'List[int]':
        hmp = {}
        output = [1] * n
        for s, e in edges:
            if s not in hmp: hmp[s] = []
            if e not in hmp: hmp[e] = []
            hmp[s].append(e)
            hmp[e].append(s)

        def dfs(output, hmp, node, labels, path):
            if node not in hmp:  # reach the leaf
                return {labels[node]: 1}
            else:  # to find how many below
                val = labels[node]
                curr = {val: 1}
                for c in hmp[node]:
                    if c not in path:
                        path.add(c)
                        child = dfs(output, hmp, c, labels, path)  # return the subtree labels hashmap
                        for k, v in child.items():
                            if k not in curr:
                                curr[k] = 0
                            curr[k] += v
                        path.remove(c)

                output[node] = curr[val]
                return curr

        path = {0}
        dfs(output, hmp, 0, labels, path)
        return output
