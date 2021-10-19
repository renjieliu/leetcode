# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root == None: return 0

        def sumChildren(output, node):
            if node.left == node.right == None:
                output.append(0)
                return node.val
            l = r = 0
            if node.left:
                l = sumChildren(output, node.left)
            if node.right:
                r = sumChildren(output, node.right)
            output.append(abs(l - r))
            return l + r + node.val

        output = []
        sumChildren(output, root)
        # print(output)
        return sum(output)
