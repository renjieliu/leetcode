class Solution:
    def equationsPossible(self, equations: 'List[str]') -> bool:
        def find(root, v):
            if v not in root:
                root[v] = v
            elif root[v]!=v: #find the real root of the v
                root[v] = find(root, root[v])
            return root[v]

        def union(root, a, b): # connect to the smaller letter
            root_a = find(root, a)
            root_b = find(root, b)
            if root_a <= root_b:
                old = root_b
                new = root_a
            else:
                old = root_a
                new = root_b

            for k in root.keys():
                if root[k] ==old:
                    root[k] = new

        root = {}
        arr = [e for e in equations if e[1] == "="]
        # print(arr)
        for e in arr: #union the ones with "==" first
            a = min(e[0],e[-1])
            b = max(e[0],e[-1])
            union(root, a, b)

        #print(root)

        arr = [e for e in equations if e[1] == "!"]
        # print(arr)
        for e in arr: #check the one should not be on the same tree
            a = min(e[0],e[-1])
            b = max(e[0],e[-1])
            if a == b:
                return False
            if a in root and b in root:
                if find(root, a) == find(root, b):
                    return False
            else:
                root[a] = root[a] if a in root else a #add itself to a separate tree, if it does not already exist
                root[b] = root[b] if b in root else b

        return True


