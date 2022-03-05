"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root == None:
            return None 
        else:
            copied = Node(root.val)
            arr = []
            for c in root.children: #for each child, make a copy of it and append to the children 
                arr.append(self.cloneTree(c))
            copied.children = arr
            return copied
    



# previous approach

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []
# """


# class Solution:
#     def cloneTree(self, root: 'Node') -> 'Node':
#         def dfs(output, node):
#             if node.children == None:
#                 return
#             else:
#                 output.children = []
#                 for i, c in enumerate(node.children):
#                     output.children.append(Node(c.val))
#                     dfs(output.children[i], c)

#         if root == None:
#             return None
#         else:
#             output = Node(root.val)
#             dfs(output, root)
#             return output

