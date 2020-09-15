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
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        def helper_up(node):
            if node.parent == None:
                return None
            else:
                if node == node.parent.left:
                    return node.parent
                else:
                    return helper_up(node.parent)

        def helper_down(node):
            if node.left == None:
                return node
            else:
                if node.left:
                    return helper_down(node.left)

        if node.right:
            return helper_down(node.right)
        else:
            return helper_up(node)
