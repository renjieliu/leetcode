# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def flat(node, output, depth):
            if node.left == node.right == None:
                output[-1] = max(output[-1], depth)
            else:
                if node.left != None: flat(node.left, output, depth+1)
                if node.right != None: flat(node.right, output, depth+1)
        output = [0]
        if root == None: return 0
        flat(root, output, 1)
        return output[-1]