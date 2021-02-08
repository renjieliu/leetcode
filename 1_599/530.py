# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def flat(node, output):
            if node.left == node.right ==None:
                output.append (node.val)
            else:
                output.append(node.val)
                if node.left:
                    flat(node.left, output)
                if node.right:
                    flat(node.right, output)
        output = []
        flat(root, output)
        output.sort()
        res = float('inf')
        for i in range(1, len(output)):
            res = min(output[i] - output[i-1], res)
        return res
