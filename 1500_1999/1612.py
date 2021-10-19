# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def flat(output, node):
            if node.val!="+":
                output.append(node.val)
            if node.left:
                flat(output, node.left)
            if node.right:
                flat(output, node.right)
        a = []
        b = []
        flat(a,root1)
        flat(b,root2)
        return sorted(a) == sorted(b)

