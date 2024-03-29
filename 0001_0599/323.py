class Solution:
    def countComponents(self, n: int, edges: 'List[List[int]]') -> int: # O( N**2 | N )
        def find(root, v): 
            if root[v] != v:
                root[v] = find(root, root[v])
            return root[v]
        
        def union(root, a, b): #union onto the smaller root
            root_a = find(root, a)
            root_b = find(root, b)
            if root_a < root_b:
                for i in range(len(root)):
                    if root[i] == root_b:
                        root[i] = root_a
            if root_b < root_a:
                for i in range(len(root)):
                    if root[i] == root_a:
                        root[i] = root_b
    
        root = [_ for _ in range(n)] 
        for a, b in edges:
            union(root, a, b)
        return len(set(root))


    






# previous solution

# class Solution:
#     def countComponents(self, n: int, edges: 'List[List[int]]') -> int:
#         tree = [-1 for _ in range(n)]
#         size = [1 for _ in range(n)]

#         def find(n, tree):
#             path = []
#             while tree[n] != -1:  # find the root parent
#                 path.append(n)
#                 n = tree[n]
#             for p in path:  # everything in the path will have the same root parent
#                 tree[p] = n
#             return n

#         def union(a, b, tree):
#             p_a = find(a, tree)
#             p_b = find(b, tree)
#             if p_a != p_b:  # they have different parent
#                 size_a = size[p_a]
#                 size_b = size[p_b]
#                 if size_a >= size_b:
#                     size[p_a] += size[p_b]
#                     size[p_b] = 0
#                     tree[p_b] = p_a
#                 else:
#                     size[p_b] += size[p_a]
#                     size[p_a] = 0
#                     tree[p_a] = p_b

#         for a, b in edges:
#             union(a, b, tree)

#         return len(size) - size.count(0)  # if the node has a parent, the size becomes 0



