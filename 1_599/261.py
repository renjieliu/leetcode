class Solution:
    def validTree(self, n: int, edges: 'List[List[int]]') -> bool:
        if n == 1:
            return True

        root = [_ for _ in range(n)]
        seen = set()

        def find(root, v):
            if root[v] != v:
                root[v] = find(root, root[v])
            return root[v]

        def union(root, a, b):
            p_a = find(root, a)
            p_b = find(root, b)
            if p_a != p_b:
                root[p_b] = p_a

        for a, b in edges:
            seen.add(a)
            seen.add(b)
            if find(root, a) == find(root, b):  # there's a loop
                return False
            else:
                union(root, a, b)

        # print(root)

        totalRoots = set()

        for i in range(n):
            realRoot = find(root, i)
            # print(i, realRoot)
            totalRoots.add(realRoot)
        return len(totalRoots) == 1 and len(seen) == n  # all the nodes are on the same tree

