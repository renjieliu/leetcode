"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]': # O( N | N )
        def dfs(output, node, lvl): #go through each node, and add to the output array
            if node:
                if len(output) == lvl:
                    output.append([node.val])
                else:
                    output[lvl].append(node.val)
                for c in node.children: # go through all the children, and add to the output
                    dfs(output, c, lvl+1)
        
        output = []
        dfs(output, root, 0) # root is at level 0
        return output
    

                    


# previous solution

# # Definition for a Node.
# class Node: #RL 20210806: BFS.
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

# class Solution:
#     def levelOrder(self, root: 'Node') -> 'List[List[int]]':
#         if root == None:
#             return []
#         output = []
#         stk = [[root]]
#         while stk:
#             output.append([])
#             nxt = [[]]
#             nodes = stk.pop(0)
#             for n in nodes:
#                 output[-1].append(n.val)
#                 for c in n.children:
#                     nxt[-1].append(c)
#             if nxt != [[]]:
#                 stk=nxt
#             else:
#                 return output
#         #return output



# previous approach 20210806: # DFS
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
#
# class Solution: #DFS
#     def levelOrder(self, root: 'Node') -> 'List[List[int]]':
#         def dfs(hmp, level, node):
#             if level not in hmp:
#                 hmp[level] = []
#             hmp[level].append(node.val)
#             for c in node.children:
#                 dfs(hmp, level+1, c)
#
#         if root == None:
#                return []
#         hmp = {}
#         dfs(hmp, 0, root)
#         m = max(hmp.keys())
#         output= []
#         for i in range(m+1):
#             output.append(hmp[i])
#         return output




# previous approach BFS
#
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
#
#
#
# class Solution:
#     def levelOrder(self, root: 'Node') -> 'List[List[int]]':
#         if root == None: return []
#         output = []
#         layers = [[root]]
#         while layers:  # using BFS to traverse
#             currLayer = layers.pop(0)
#             output.append([])
#             for node in currLayer:
#                 output[-1].append(node.val)
#                 for c in node.children:  # it has children and need to be added to the next layer
#                     if layers == []:
#                         layers.append([])
#                     layers[-1].append(c)
#
#         return output




