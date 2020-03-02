# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if node:
                if node.left or node.right:
                    t = node.left
                    node.left = node.right
                    node.right = t
                    invert(node.left)
                    invert(node.right)

        invert(root)
        return root

