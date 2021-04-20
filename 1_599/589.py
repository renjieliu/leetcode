"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> 'List[int]':
        def helper(output, node):
            if node:
                output.append(node.val)
                for n in node.children:
                    helper(output, n)
        output = []
        helper(output, root)
        return output


