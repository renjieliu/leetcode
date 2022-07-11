"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':  #O( H | 1 )  H is the height of the tree
        if node.right: #the next node is on the left-most leaf on the right child tree
            node = node.right
            while node.left:
                node = node.left
            return node 
        
        else: #if it does not have a right child tree, the result is one of the parent nodes
            while node.parent and node == node.parent.right:
                node = node.parent
            if node.parent: #current node is the left node of the parent
                return node.parent 
            
        return None
    



# previous solution

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None
# """


# class Solution:
#     def inorderSuccessor(self, node: 'Node') -> 'Node':
#         def helper_up(node):
#             if node.parent == None:
#                 return None
#             else:
#                 if node == node.parent.left:
#                     return node.parent
#                 else:
#                     return helper_up(node.parent)

#         def helper_down(node):
#             if node.left == None:
#                 return node
#             else:
#                 if node.left:
#                     return helper_down(node.left)

#         if node.right:
#             return helper_down(node.right)
#         else:
#             return helper_up(node)


