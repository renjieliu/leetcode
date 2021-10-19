class Solution:
    def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
        def find(root, v):
            if root[v] != v:
                root[v] = find(root, root[v])
            return root[v]

        def union(root, size, a, b):
            root_a = root[a]
            root_b = root[b]
            if size[root_a] >= size[root_b]:
                root[root_b] = root_a
                size[root_a]+=size[root_b]
            else:
                root[root_a] = root_b
                size[root_b] += size[root_a]

        size = defaultdict(lambda: 1) #total nodes is unknown beforehand, initialize the size of it once called.
        root = {} #total nodes is unknown beforehand, initialize the root for it once called.
        output = []
        for a, b in edges:
            if a not in root:
                root[a] = a
            if b not in root:
                root[b] = b

            if find(root, a) == find(root, b): #a cycle is found
                output = [a,b]
            else:
                union(root,size, a, b)
        return output



# previous approach
# class Solution:
#     def findRedundantConnection(self, edges: 'List[List[int]]') -> 'List[int]':
#         trees = [edges[0]] #initialize the tree
#         i = 1
#         while i < len(edges): #go through the edge list
#             #print(trees)
#             find = []
#             j = 0
#             while j < len(trees): # check if match with any current tree
#                 t = trees[j]
#                 #print('t - ', t)
#                 if edges[i][0] in t and edges[i][1] in t: #redudant connection. both nodes are in current tree
#                     return edges[i]
#                 elif edges[i][0] in t or edges[i][1] in t: #add to the tree
#                     t+=edges[i]
#                     find.append(j)
#                 j+=1
#             if find == []: #new node, cannot find any match
#                 trees.append(edges[i])
#             elif len(find) == 2: # current one is the bridge, need to merge both trees
#                 trees[find[0]]+=trees[find[1]]
#                 trees = trees[:find[1]] + trees[find[1]+1:]
#             i+=1