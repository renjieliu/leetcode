class Solution: 
    def sumOfDistancesInTree(self, n: int, edges: 'List[List[int]]') -> 'List[int]': # O( N | N )
        graph = defaultdict(lambda: set())
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        ans = [0] * n
        def dfs(count, ans, graph, node, parent):
            for child in graph[node]:
                if child != parent: # avoid loop
                    dfs(count, ans, graph, child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child] #answer of child + how many nodes below (steps from curr to reach all the nodes below)

        def dfs2(count, ans, graph, node, parent):
            for child in graph[node]:
                if child!=parent: # avoid loop
                    ans[child] = (ans[node] - count[child]) + (n - count[child]) # curr - child branch + (remaining count)
                    dfs2(count, ans, graph, child, node)

        dfs(count, ans, graph, 0, None)
        dfs2(count, ans, graph, 0 , None)
        return ans






# previous solution

# class Solution: 
#     def sumOfDistancesInTree(self, n: int, edges: 'List[List[int]]') -> 'List[int]': #RL 20221221: Copied solution, O( N | N )
#         graph = defaultdict(lambda: set())
#         for u, v in edges:
#             graph[u].add(v)
#             graph[v].add(u)

#         count = [1] * n
#         ans = [0] * n
#         def dfs(node = 0, parent = None):
#             for child in graph[node]:
#                 if child != parent:
#                     dfs(child, node)
#                     count[node] += count[child]
#                     ans[node] += ans[child] + count[child]

#         def dfs2(node = 0, parent = None):
#             for child in graph[node]:
#                 if child != parent:
#                     ans[child] = ans[node] - count[child] + n - count[child]
#                     dfs2(child, node)

#         dfs()
#         dfs2()
#         return ans



# previous solution

# class Solution:  # RL 20210904: Copied solution
#     def sumOfDistancesInTree(self, n: int, edges: 'List[List[int]]') -> 'List[int]':
#         graph = defaultdict(lambda: set())
#         for u, v in edges:
#             graph[u].add(v)
#             graph[v].add(u)

#         count = [1] * n
#         ans = [0] * n

#         def dfs(node=0, parent=None):
#             for child in graph[node]:
#                 if child != parent:
#                     dfs(child, node)
#                     count[node] += count[child]
#                     ans[node] += ans[child] + count[child]

#         def dfs2(node=0, parent=None):
#             for child in graph[node]:
#                 if child != parent:
#                     ans[child] = ans[node] - count[child] + n - count[child]
#                     dfs2(child, node)

#         dfs()
#         dfs2()
#         return ans



