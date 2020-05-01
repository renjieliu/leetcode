# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, left, right):  # node, leftboundary and rightboundary
            if node.left == node.right == None:
                return True if left < node.val < right else False
            else:
                if node.left:
                    if left < node.left.val < node.val:
                        if validate(node.left, left, node.val) == False: return False
                    else:
                        return False
                if node.right:
                    if node.val < node.right.val < right:
                        if validate(node.right, node.val, right) == False: return False
                    else:
                        return False
                return True

        if root == None:
            return True
        else:
            return validate(root, -float('inf'), float('inf'))
