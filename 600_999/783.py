# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def flat(node, output):
            if node.left ==node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.left!=None:
                    flat(node.left, output)
                if node.right!=None:
                    flat(node.right, output)
        output = []
        flat(root, output)
        output.sort()
        res = float('inf')
        for i in range(1, len(output)):
            res = min(res, output[i] - output[i-1])
        return res