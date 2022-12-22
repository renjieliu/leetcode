class Solution:
    def validPath(self, n: int, edges: 'List[List[int]]', source: int, destination: int) -> bool: # O( N | N )
        from_to = defaultdict(lambda:[])  
        for a, b in edges: # flat the edges array, to record the nxt nodes from curr
            from_to[a].append(b)
            from_to[b].append(a)
        
        def dfs(seen, from_to, curr, destination): # dfs from curr node to destination
            if curr == destination:
                seen[curr] = True 
                return seen[curr]
            else:
                seen[curr] = False
                for nxt in from_to[curr]:
                    if nxt not in seen:
                        seen[curr] = dfs(seen, from_to, nxt, destination)
                        if seen[curr]:
                            return True
                return seen[curr]
        
        return dfs({}, from_to, source, destination)
    




# previous solution

# class Solution:
#     def validPath(self, n: int, edges: 'List[List[int]]', start: int, end: int) -> bool:
#         def find(root, v):
#             if root[v]!=v:
#                 root[v] = find(root,  root[v])
#             return root[v]

#         def union(root, a, b):
#             p_a = find(root, a)
#             p_b = find(root, b)
#             if p_a!=p_b:
#                 root[p_b] = p_a

#         root = [_ for _ in range(n)]

#         for a, b in edges:
#             union(root, a, b)

#         return find(root, start) == find(root, end)


# previous approach
# class Solution:  # union find approach
#     def validPath(self, n: int, edges: 'List[List[int]]', start: int, end: int) -> bool:
#         def find(root, v):
#             if root[v] != v:
#                 root[v] = find(root, root[v])
#             return root[v]
#
#         root = list(range(n))
#         for n1, n2 in edges:
#             p_a = find(root, n1)
#             p_b = find(root, n2)
#             if p_a != p_b:
#                 root[p_b] = p_a
#
#         return find(root, start) == find(root, end)

# class Solution: #BFS approach
#     def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
#         if start == end:
#             return True
#         hmp = {}
#         for a, b in edges:
#             if a not in hmp:
#                 hmp[a]=[]
#             hmp[a].append(b)
#             if b not in hmp:
#                 hmp[b] = []
#             hmp[b].append(a)
#         stk = [start]
#         seen = {start}
#         while stk:
#             nxt = []
#             while stk:
#                 v = stk.pop(0)
#                 if v in hmp:
#                     for x in hmp[v]:
#                         if x == end :
#                             return True
#                         elif x not in seen:
#                             seen.add(x)
#                             nxt.append(x)
#             stk = nxt
#         return False


