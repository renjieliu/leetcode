# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def flat(output, node, maxx, minn):
            if node.left == node.right == None:
                output[0] = max(output[0], max(maxx, node.val) - min(minn, node.val))
            else:
                if node.left:
                    flat(output, node.left, max(maxx, node.val), min(minn, node.val))
                if node.right:
                    flat(output, node.right, max(maxx, node.val), min(minn, node.val))

        output = [-float('inf')]
        flat(output, root, root.val, root.val)
        return output[0]
