# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, curr, flat) :
            if node.left == node.right:
                flat.append( int(''.join(curr)+str(node.val)))
            else:
                if node.left:helper(node.left, curr+[str(node.val)], flat)
                if node.right:helper(node.right, curr+[str(node.val)], flat)
        if root == None: return 0
        else:
            flat = []
            helper(root, [], flat)
            return sum(flat)