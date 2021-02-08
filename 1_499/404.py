# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def flat(node, output, direction):
            if node.left == node.right == None:
                output[-1] += node.val if direction == 1 else 0
            else:
                if node.left:
                    flat(node.left, output, 1)
                if node.right:
                    flat(node.right, output, 2)

        if root == None:
            return 0
        else:
            output = [0]
            flat(root, output, 0)
            return output[0]
