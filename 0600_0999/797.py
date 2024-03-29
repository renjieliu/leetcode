class Solution:
    def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]': # O( N*2**N | N )
        def dfs(output, curr, graph, path): # no need to check if there's loop, as it's DAG
            if curr == len(graph)-1: # it has reached the end (n)
                output.append(path) 
            else:
                for nxt in graph[curr]:
                    dfs(output, nxt, graph, path + [nxt]) 
        output = []
        dfs(output, 0, graph, [0])
        return output 
            



# previous solution

# class Solution:
#     def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
#         output = [] 
#         def helper(output, i, path, graph):
#             if i == len(graph)-1: # if current node is the last node of the graph
#                 output.append(path)
#             else:
#                 for n in graph[i]: #for each node in the graph, search for the next
#                     helper(output, n, path + [n], graph)
        
#         helper(output, 0, [0], graph) # starting from node 0
#         return output
    



# previous approach
# class Solution:
#     def allPathsSourceTarget(self, graph: 'List[List[int]]') -> 'List[List[int]]':
#         hmp = {}
#         for i, c in enumerate(graph):
#             if len(c) > 0:
#                 if i not in hmp:
#                     hmp[i] = []
#                 for to in c:
#                     hmp[i].append(to)

#         def dfs(output, hmp, node, path, target):
#             if node not in hmp:
#                 return -1
#             else:
#                 for c in hmp[node]:
#                     if c == target:
#                         output.append(path + [c])
#                     else:
#                         dfs(output, hmp, c, path + [c], target)

#         output = []
#         dfs(output, hmp, 0, [0], len(graph) - 1)
#         return output

# previous approach
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         def dfs(graph, curr_pos, curr_path, output):
#             if curr_pos == len(graph) - 1:  # it has reached the end of the array
#                 output.append(curr_path)
#             elif graph[curr_pos] == []:  # in the middle of the array, and it's blank, return.
#                 return []
#             else:
#                 for i in range(len(graph[curr_pos])):  # iterate thru the curr node
#                     nxt_pos = graph[curr_pos][i]
#                     dfs(graph, nxt_pos, curr_path + [nxt_pos], output)
#                 return output
#
#         return dfs(graph, 0, [0], [])  # start from position 0