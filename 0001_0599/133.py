"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(built, node):
            curr = Node(node.val) 
            built[curr.val] = curr #put current into the hashmap 
            for n in node.neighbors:
                if n.val not in built: # if the value is seen, no need to build it, to avoid infinite loop
                    curr.neighbors.append(helper(built, n))
                else:
                    curr.neighbors.append(built[n.val]) #just add it to the neighbors
            return curr

        return helper({}, node) if node else None
    

    
    


# previous approach

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         def dfs(node, hmp):
#             for n in node.neighbors:
#                 if n not in hmp:
#                     hmp[n] = Node(n.val)
#                     dfs(n, hmp)
#                 hmp[node].neighbors.append(hmp[n])


#         if node == None:
#             return None
#         hmp = { node: Node(node.val) }
#         dfs(node, hmp)
#         return hmp[node]



