class Solution:
    def isBipartite(self, graph: 'List[List[int]]') -> bool: #O(N | N)
        def dfs(hmp, node, color, graph): #current dfs cannot be the same as the parent
            if node in hmp:
                if hmp[node] == color:
                    return True 
                else:
                    return False
            hmp[node] = color
            for nxt in graph[node]:
                if dfs(hmp, nxt, -color, graph) == False:
                    return False
            return True

        
        hmp = {}
        for i in range(len(graph)):
            if i not in hmp:
                if dfs(hmp, i, 1, graph) == False:
                    return False                
        return True



# previous approach
        
# class Solution:
#     def isBipartite(self, graph: 'List[List[int]]') -> bool:
#         hmp = {}
#         for i in range(len(graph)):
#             if i not in hmp:
#                 hmp[i] = 0
#                 stk = [i]
#                 while stk:
#                     node = stk.pop(0)  # self
#                     for n in graph[node]:  # all the connected nodes
#                         if n not in hmp:
#                             stk.append(n)
#                             hmp[n] = hmp[node] ^ 1
#                         elif hmp[n] == hmp[node]:  # same as the reference
#                             return False
#         return True

# previous approach
# class Solution(object):
#     def isBipartite(self, graph):
#         color = {}
#         for node in range(len(graph)):
#             if node not in color:
#                 stack = [node]
#                 color[node] = 0
#                 while stack:
#                     node = stack.pop()
#                     for nei in graph[node]:
#                         if nei not in color:
#                             stack.append(nei)
#                             color[nei] = color[node] ^ 1
#                         elif color[nei] == color[node]:
#                             return False
#         return True