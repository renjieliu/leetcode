class Solution:
    def findMinHeightTrees(self, n: int, edges: 'List[List[int]]') -> 'List[int]':
        if n <= 2: #this is already the centroids we are looking for
            return [_ for _ in range(n)] 
        
        else: #topological sort, from leaf to the centroids, until there's <= 2 nodes left
            adj = [set() for _ in range(n)]
            for a, b in edges:
                adj[a].add(b)
                adj[b].add(a)
            rem = n
            stk = []
            for i, a in enumerate(adj): 
                if len(a) == 1: #it only has one neighbour
                    stk.append(i)
            while rem > 2:
                nxt = []
                rem -= len(stk)
                while stk:
                    currLeaf = stk.pop()
                    for neighbour in adj[currLeaf]:
                        adj[neighbour].remove(currLeaf)
                        if len(adj[neighbour]) == 1:
                            nxt.append(neighbour)
                stk = nxt
            
            return stk #the remaining stk is the centroids we are looking for
        


# previous approach
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: 'List[List[int]]') -> 'List[int]':

#         # base cases
#         if n <= 2:
#             return [i for i in range(n)]

#         # Build the graph with the adjacency list
#         neighbors = [set() for i in range(n)]
#         for start, end in edges:
#             neighbors[start].add(end)
#             neighbors[end].add(start)

#         # Initialize the first layer of leaves
#         leaves = []
#         for i in range(n):
#             if len(neighbors[i]) == 1:
#                 leaves.append(i)

#         # Trim the leaves until reaching the centroids
#         remaining_nodes = n
#         while remaining_nodes > 2:
#             remaining_nodes -= len(leaves)
#             new_leaves = []
#             # remove the current leaves along with the edges
#             while leaves:
#                 leaf = leaves.pop()
#                 for neighbor in neighbors[leaf]:
#                     neighbors[neighbor].remove(leaf)
#                     if len(neighbors[neighbor]) == 1:
#                         new_leaves.append(neighbor)

#             # prepare for the next round
#             leaves = new_leaves

#         # The remaining nodes are the centroids of the graph
#         return leaves



