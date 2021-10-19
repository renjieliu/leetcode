# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def flat(output, node, target): #output: [diff, value]
            if node.left== node.right == None:
                if abs(node.val - target) < output[0]:
                    output[0] = abs(node.val - target)
                    output[1] = node.val
            else:
                if abs(node.val - target) < output[0]:
                    output[0] = abs(node.val - target)
                    output[1] = node.val
                if node.left:
                    flat(output, node.left, target)
                if node.right:
                    flat(output, node.right, target)
        output = [float('inf'), None]
        flat(output, root, target)
        return output[1]